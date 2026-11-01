"""Conservative syntax analysis. A static reference is not a runtime guarantee."""
from __future__ import annotations
import ast
from collections import defaultdict


def dotted_name(node):
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = dotted_name(node.value)
        return f"{prefix}.{node.attr}" if prefix != "<dynamic>" else "<dynamic>"
    return "<dynamic>"


class SymbolVisitor(ast.NodeVisitor):
    def __init__(self):
        self.scope = ""
        self.scopes = {"": {"parent": None, "kind": "module", "bindings": defaultdict(list)}}
        self.symbols, self.calls, self.imports = [], [], []

    def bind(self, name, binding):
        self.scopes[self.scope]["bindings"][name].append(binding)

    def definition(self, node, kind):
        qualified = f"{self.scope}.{node.name}".lstrip(".")
        self.bind(node.name, {"kind": "definition", "name": qualified})
        for decorator in node.decorator_list:
            self.visit(decorator)
        if isinstance(node, ast.ClassDef):
            for base in node.bases:
                self.visit(base)
            for keyword in node.keywords:
                self.visit(keyword.value)
            signature = node.name
        else:
            for default in [*node.args.defaults, *node.args.kw_defaults]:
                if default is not None:
                    self.visit(default)
            signature = f"{node.name}({ast.unparse(node.args)})"
        self.symbols.append({"name": qualified, "kind": kind,
                             "line": min([node.lineno] + [d.lineno for d in node.decorator_list]),
                             "definition_line": node.lineno, "end_line": node.end_lineno,
                             "signature": signature[:500], "docstring": (ast.get_docstring(node) or "")[:800]})
        previous, self.scope = self.scope, qualified
        self.scopes.setdefault(qualified, {"parent": previous, "kind": kind, "bindings": defaultdict(list)})
        if not isinstance(node, ast.ClassDef):
            args = [*node.args.posonlyargs, *node.args.args, *node.args.kwonlyargs]
            args += [a for a in (node.args.vararg, node.args.kwarg) if a]
            for arg in args:
                self.bind(arg.arg, {"kind": "unknown", "reason": "parameter"})
        for statement in node.body:
            self.visit(statement)
        self.scope = previous

    def visit_FunctionDef(self, node):
        self.definition(node, "function")

    def visit_AsyncFunctionDef(self, node):
        self.definition(node, "async_function")

    def visit_ClassDef(self, node):
        self.definition(node, "class")

    def visit_Name(self, node):
        if isinstance(node.ctx, (ast.Store, ast.Del)):
            self.bind(node.id, {"kind": "unknown", "reason": "assigned or deleted name"})

    def visit_Global(self, node):
        for name in node.names:
            self.bind(name, {"kind": "unknown", "reason": "global declaration"})

    def visit_Nonlocal(self, node):
        for name in node.names:
            self.bind(name, {"kind": "unknown", "reason": "nonlocal declaration"})

    def visit_ExceptHandler(self, node):
        if node.name:
            self.bind(node.name, {"kind": "unknown", "reason": "exception binding"})
        self.generic_visit(node)

    def visit_MatchAs(self, node):
        if node.name:
            self.bind(node.name, {"kind": "unknown", "reason": "pattern binding"})
        self.generic_visit(node)

    def visit_MatchStar(self, node):
        if node.name:
            self.bind(node.name, {"kind": "unknown", "reason": "pattern binding"})

    def visit_MatchMapping(self, node):
        if node.rest:
            self.bind(node.rest, {"kind": "unknown", "reason": "pattern binding"})
        self.generic_visit(node)

    def visit_Lambda(self, node):
        previous = self.scope
        qualified = f"{previous}.<lambda@{node.lineno}:{node.col_offset}>".lstrip(".")
        self.scope = qualified
        self.scopes[qualified] = {"parent": previous, "kind": "lambda", "bindings": defaultdict(list)}
        for arg in [*node.args.posonlyargs, *node.args.args, *node.args.kwonlyargs,
                    *[a for a in (node.args.vararg, node.args.kwarg) if a]]:
            self.bind(arg.arg, {"kind": "unknown", "reason": "lambda parameter"})
        self.visit(node.body)
        self.scope = previous

    def visit_Import(self, node):
        for alias in node.names:
            bound = alias.asname or alias.name.split(".")[0]
            record = {"module": alias.name, "alias": alias.asname, "line": node.lineno,
                      "scope": self.scope, "level": 0, "member": None}
            self.imports.append(record)
            self.bind(bound, {"kind": "import", "module": alias.name if alias.asname else bound,
                              "level": 0, "member": None})

    def visit_ImportFrom(self, node):
        for alias in node.names:
            record = {"module": node.module or "", "level": node.level,
                      "member": alias.name, "alias": alias.asname, "line": node.lineno,
                      "scope": self.scope}
            self.imports.append(record)
            if alias.name != "*":
                self.bind(alias.asname or alias.name, {"kind": "import", **record})
            else:
                self.scopes[self.scope]["wildcard_import"] = True

    def visit_Call(self, node):
        self.calls.append({"caller": self.scope or "<module>", "scope": self.scope,
                           "callee_spelling": dotted_name(node.func), "line": node.lineno,
                           "column": node.col_offset})
        self.generic_visit(node)


def module_name(path):
    parts = path.removesuffix(".py").split("/")
    if parts[0] == "src":
        parts = parts[1:]
    if parts and parts[-1] == "__init__":
        parts.pop()
    return ".".join(parts)


def absolute_import(record, data):
    if not record["level"]:
        return record["module"]
    package = data["module"] if data["is_package"] else data["module"].rpartition(".")[0]
    parts = package.split(".") if package else []
    if record["level"] > len(parts):
        return None
    base = parts[:len(parts)-record["level"]+1]
    return ".".join([*base, *([record["module"]] if record["module"] else [])])


class Resolver:
    def __init__(self, files):
        self.files = files
        self.modules = defaultdict(list)
        for path, data in files.items():
            self.modules[data["module"]].append(path)

    def symbol(self, path, name):
        matches = [s for s in self.files[path]["symbols"] if s["name"] == name]
        if len(matches) != 1:
            return None
        s = matches[0]
        return {"path": path, "name": name, "line": s["definition_line"],
                "citation": f"{path}:{s['definition_line']}"}

    def binding(self, path, scope, name):
        scopes, current, first = self.files[path]["scopes"], scope, True
        while current is not None:
            item = scopes[current]
            if first or item["kind"] != "class":
                if item.get("wildcard_import"):
                    return {"kind": "unknown", "reason": "wildcard import may replace bindings"}
                choices = item["bindings"].get(name, [])
                if len(choices) == 1:
                    return choices[0]
                if choices:
                    return {"kind": "unknown", "reason": "ambiguous or rebound name"}
            current, first = item["parent"], False
        return {"kind": "unknown", "reason": "no supported lexical binding"}

    def reference(self, path, scope, spelling, seen=()):
        key = (path, scope, spelling)
        if key in seen or len(seen) >= 12:
            return None, "cyclic or deep import chain"
        parts = spelling.split(".")
        binding = self.binding(path, scope, parts[0])
        if binding["kind"] == "unknown":
            return None, binding["reason"]
        rest = parts[1:]
        if binding["kind"] == "definition":
            target = self.symbol(path, ".".join([binding["name"], *rest]))
            return target, "lexical declaration" if target else "unsupported attribute or ambiguous definition"
        base = absolute_import(binding, self.files[path])
        if base is None:
            return None, "relative import outside inferred package"
        qualified = ".".join(p for p in [base, binding["member"], *rest] if p)
        pieces = qualified.split(".")
        for count in range(len(pieces), 0, -1):
            paths = self.modules.get(".".join(pieces[:count]), [])
            if not paths:
                continue
            if len(paths) != 1:
                return None, "ambiguous module roots"
            suffix = pieces[count:]
            if not suffix:
                return None, "import refers to a module, not a declaration"
            target, reason = self.reference(paths[0], "", ".".join(suffix), (*seen, key))
            return target, "import alias to " + reason
        return None, "external or unindexed module"

    def enrich(self):
        for path, data in self.files.items():
            for call in data["calls"]:
                if call["callee_spelling"] == "<dynamic>":
                    target, reason = None, "dynamic callable expression"
                else:
                    target, reason = self.reference(path, call["scope"], call["callee_spelling"])
                call["resolution"] = {"status": "static_reference" if target else "unresolved",
                                      "reason": reason, "target": target}
                call["citation"] = f"{path}:{call['line']}"
            for record in data["imports"]:
                module = absolute_import(record, data)
                record["absolute_module"] = module
                candidates = self.modules.get(module, []) if module else []
                if record["member"] and module:
                    candidates = self.modules.get(f"{module}.{record['member']}", []) or candidates
                record["indexed_paths"] = candidates if len(candidates) == 1 else []
                record["citation"] = f"{path}:{record['line']}"
