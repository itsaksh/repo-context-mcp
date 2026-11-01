"""A bounded read-only snapshot of Python source; no indexed code is executed."""
from __future__ import annotations
import ast
import hashlib
import os
from pathlib import Path, PurePosixPath
import tokenize
from .analysis import Resolver, SymbolVisitor, module_name

IGNORED = {".git", ".venv", "venv", "node_modules", "__pycache__", "build", "dist", ".tox"}


def integer(value, name, minimum, maximum):
    if type(value) is not int or not minimum <= value <= maximum:
        raise ValueError(f"{name} must be an integer from {minimum} to {maximum}")


def query_text(value, allow_empty=True):
    if not isinstance(value, str) or len(value) > 200 or (not allow_empty and not value.strip()):
        raise ValueError("query must be text, at most 200 characters, and nonempty for code search")


class RepositoryIndex:
    def __init__(self, root, max_files=500, max_file_bytes=262_144, max_total_bytes=16_777_216):
        integer(max_files, "max_files", 1, 5000)
        integer(max_file_bytes, "max_file_bytes", 1, 1_048_576)
        integer(max_total_bytes, "max_total_bytes", 1, 67_108_864)
        self.root = Path(root).resolve(strict=True)
        if not self.root.is_dir():
            raise ValueError("Repository root must be a directory")
        self.files, self.skipped = {}, []
        self.truncated, self.total_bytes = False, 0
        self.limits = {"max_files": max_files, "max_file_bytes": max_file_bytes, "max_total_bytes": max_total_bytes}
        stop = False
        for directory, dirs, files in os.walk(self.root, followlinks=False):
            if stop:
                break
            if not Path(directory).resolve().is_relative_to(self.root):
                dirs[:] = []
                continue
            dirs[:] = sorted(d for d in dirs if d not in IGNORED and not (Path(directory)/d).is_symlink())
            for filename in sorted(files):
                path = Path(directory)/filename
                if path.suffix != ".py" or path.is_symlink() or not path.resolve().is_relative_to(self.root):
                    continue
                relative = path.relative_to(self.root).as_posix()
                if len(self.files) >= max_files:
                    self.truncated = stop = True
                    break
                try:
                    size = path.stat().st_size
                    if size > max_file_bytes:
                        self.skipped.append({"path": relative, "reason": "file size limit"})
                        continue
                    if self.total_bytes+size > max_total_bytes:
                        self.truncated = stop = True
                        break
                    with tokenize.open(path) as stream:
                        source = stream.read(max_file_bytes+1)
                    source_bytes = source.encode("utf-8")
                    if len(source_bytes) > max_file_bytes:
                        self.skipped.append({"path": relative, "reason": "decoded source size limit"})
                        continue
                    if self.total_bytes+len(source_bytes) > max_total_bytes:
                        self.truncated = stop = True
                        break
                    tree = ast.parse(source, filename=relative)
                    visitor = SymbolVisitor()
                    visitor.visit(tree)
                    self.total_bytes += len(source_bytes)
                    self.files[relative] = {"module": module_name(relative), "is_package": path.name == "__init__.py",
                                            "symbols": visitor.symbols, "calls": visitor.calls,
                                            "imports": visitor.imports, "scopes": visitor.scopes,
                                            "lines": source.splitlines(), "sha256": hashlib.sha256(source_bytes).hexdigest()}
                except (OSError, SyntaxError, UnicodeError, RecursionError) as exc:
                    self.skipped.append({"path": relative, "reason": type(exc).__name__})
        Resolver(self.files).enrich()
        fingerprints = "\n".join(f"{p}:{f['sha256']}" for p, f in sorted(self.files.items()))
        self.snapshot_sha256 = hashlib.sha256(fingerprints.encode("utf-8")).hexdigest()

    def file_key(self, relative):
        if not isinstance(relative, str) or not relative or len(relative) > 1024:
            raise ValueError("path must be a nonempty relative path")
        normalized = relative.replace("\\", "/")
        path = PurePosixPath(normalized)
        if path.is_absolute() or ":" in normalized or ".." in path.parts:
            raise ValueError("path must stay within the selected repository")
        key = path.as_posix()
        if key not in self.files:
            raise ValueError("path is not an indexed Python file")
        return key

    def file(self, relative):
        return self.files[self.file_key(relative)]

    def summary(self):
        calls = [c for f in self.files.values() for c in f["calls"]]
        resolved = sum(c["resolution"]["status"] == "static_reference" for c in calls)
        return {"files": len(self.files), "symbols": sum(len(f["symbols"]) for f in self.files.values()),
                "calls": len(calls), "static_references": resolved, "unresolved_calls": len(calls)-resolved,
                "skipped": self.skipped, "truncated": self.truncated, "indexed_utf8_bytes": self.total_bytes,
                "limits": self.limits, "snapshot_sha256": self.snapshot_sha256,
                "call_resolution": "Conservative static references, not runtime guarantees. Instance dispatch remains unresolved."}

    def list_symbols(self, query="", limit=20):
        query_text(query)
        integer(limit, "limit", 1, 100)
        found = []
        for path, data in sorted(self.files.items()):
            for symbol in data["symbols"]:
                if query.casefold() in symbol["name"].casefold():
                    found.append({"path": path, **symbol, "citation": f"{path}:{symbol['definition_line']}"})
        return found[:limit]

    def get_symbol_context(self, path, name, max_chars=12_000):
        integer(max_chars, "max_chars", 100, 32_000)
        key = self.file_key(path)
        data = self.files[key]
        matches = [s for s in data["symbols"] if s["name"] == name]
        if len(matches) != 1:
            raise ValueError("symbol missing or ambiguous; use a unique qualified name from list_symbols")
        symbol = matches[0]
        start, end = symbol["line"], min(symbol["end_line"], symbol["line"]+119)
        full = "\n".join(f"{i+1}: {data['lines'][i]}" for i in range(start-1, end))
        excerpt = full[:max_chars]
        return {"path": key, **symbol, "excerpt_end_line": start+excerpt.count("\n")-int(excerpt.endswith("\n")),
                "truncated": end < symbol["end_line"] or len(full) > max_chars, "source": excerpt,
                "source_characters": len(excerpt), "max_characters": max_chars,
                "citation": f"{key}:{symbol['definition_line']}", "file_sha256": data["sha256"]}

    def get_imports(self, path):
        return self.file(path)["imports"]

    def find_calls(self, query, limit=30):
        query_text(query)
        integer(limit, "limit", 1, 100)
        result = []
        for path, data in sorted(self.files.items()):
            for call in data["calls"]:
                target = call["resolution"]["target"] or {}
                if query.casefold() in (call["callee_spelling"]+" "+target.get("name", "")).casefold():
                    result.append({"path": path, **{k: v for k, v in call.items() if k != "scope"}})
        return result[:limit]

    def search_code(self, query, limit=20):
        query_text(query, allow_empty=False)
        integer(limit, "limit", 1, 100)
        found = []
        for path, data in sorted(self.files.items()):
            for line, text in enumerate(data["lines"], 1):
                if query.casefold() in text.casefold():
                    found.append({"path": path, "line": line, "text": text[:500],
                                  "truncated": len(text) > 500, "citation": f"{path}:{line}"})
                    if len(found) >= limit:
                        return found
        return found

    def get_dependencies(self, path):
        key = self.file_key(path)
        data = self.files[key]
        return {"path": key, "module": data["module"], "imports": data["imports"],
                "indexed_dependencies": sorted({p for r in data["imports"] for p in r["indexed_paths"]}),
                "note": "Import evidence only; conditional imports are not proven runtime dependencies."}

    def get_callers(self, path, name, limit=30):
        key = self.file_key(path)
        integer(limit, "limit", 1, 100)
        if len([s for s in self.files[key]["symbols"] if s["name"] == name]) != 1:
            raise ValueError("target symbol missing or ambiguous")
        found = []
        for source, data in sorted(self.files.items()):
            for call in data["calls"]:
                target = call["resolution"]["target"] or {}
                if target.get("path") == key and target.get("name") == name:
                    found.append({"path": source, **{k: v for k, v in call.items() if k != "scope"}})
        return {"target": {"path": key, "name": name}, "callers": found[:limit], "truncated": len(found) > limit,
                "note": "Only supported static references are included; unresolved calls may also reach this declaration."}
