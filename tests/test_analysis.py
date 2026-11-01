from pathlib import Path
import tempfile
import unittest
from repocontext.index import RepositoryIndex


class AnalysisTests(unittest.TestCase):
    def index(self, files, **kwargs):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        for name, source in files.items():
            path = root/name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(source, encoding="utf-8")
        return RepositoryIndex(root, **kwargs)

    def test_direct_local_call_and_callers(self):
        idx = self.index({"app.py": "def target(): pass\ndef caller():\n    target()\n"})
        call = idx.find_calls("target")[0]
        self.assertEqual(call["resolution"]["target"]["name"], "target")
        callers = idx.get_callers("app.py", "target")["callers"]
        self.assertEqual(callers[0]["citation"], "app.py:3")

    def test_relative_import_alias(self):
        idx = self.index({"pkg/__init__.py": "", "pkg/util.py": "def total(): pass",
                          "pkg/main.py": "from .util import total as calculate\ndef run():\n    calculate()"})
        target = idx.find_calls("calculate")[0]["resolution"]["target"]
        self.assertEqual((target["path"], target["name"]), ("pkg/util.py", "total"))
        self.assertEqual(idx.get_dependencies("pkg/main.py")["indexed_dependencies"], ["pkg/util.py"])

    def test_module_alias_and_src_layout(self):
        idx = self.index({"src/pkg/util.py": "def total(): pass",
                          "src/pkg/main.py": "import pkg.util as u\ndef run():\n    u.total()"})
        self.assertEqual(idx.find_calls("u.total")[0]["resolution"]["target"]["path"], "src/pkg/util.py")

    def test_reexport_through_package(self):
        idx = self.index({"pkg/__init__.py": "from .util import total", "pkg/util.py": "def total(): pass",
                          "app.py": "from pkg import total as calculate\ncalculate()"})
        self.assertEqual(idx.find_calls("calculate")[0]["resolution"]["target"]["path"], "pkg/util.py")

    def test_parameter_shadows_import(self):
        idx = self.index({"util.py": "def total(): pass",
                          "app.py": "from util import total\ndef run(total):\n    total()"})
        self.assertEqual(idx.find_calls("total")[0]["resolution"]["reason"], "parameter")

    def test_assignment_rebinding_is_not_resolved(self):
        idx = self.index({"util.py": "def total(): pass",
                          "app.py": "from util import total\ntotal = lambda: 0\ntotal()"})
        self.assertEqual(idx.find_calls("total")[0]["resolution"]["status"], "unresolved")

    def test_method_does_not_see_class_attributes_as_lexical_names(self):
        idx = self.index({"app.py": "class C:\n    def helper(self): pass\n    def run(self):\n        helper()\n        self.helper()"})
        self.assertTrue(all(c["resolution"]["status"] == "unresolved" for c in idx.find_calls("helper")))

    def test_nested_function_can_reference_enclosing_function_scope(self):
        idx = self.index({"app.py": "def outer():\n    def helper(): pass\n    def inner():\n        helper()"})
        self.assertEqual(idx.find_calls("helper")[0]["resolution"]["target"]["name"], "outer.helper")

    def test_lambda_parameter_shadows_global_function(self):
        idx = self.index({"app.py": "def target(): pass\nf = lambda target: target()"})
        self.assertEqual(idx.find_calls("target")[0]["resolution"]["reason"], "lambda parameter")

    def test_default_expression_is_in_surrounding_scope(self):
        idx = self.index({"app.py": "def make(): pass\ndef run(make=make()): pass"})
        self.assertEqual(idx.find_calls("make")[0]["caller"], "<module>")
        self.assertEqual(idx.find_calls("make")[0]["resolution"]["status"], "static_reference")

    def test_match_binding_is_not_mistaken_for_import(self):
        idx = self.index({"util.py": "def total(): pass", "app.py":
                          "from util import total\ndef run(x):\n    match x:\n        case {'total': total}:\n            total()"})
        self.assertEqual(idx.find_calls("total")[0]["resolution"]["reason"], "pattern binding")

    def test_external_and_dynamic_calls_remain_unresolved(self):
        idx = self.index({"app.py": "import outside_library as x\nx.run()\nfactory()()"})
        self.assertTrue(all(c["resolution"]["status"] == "unresolved" for c in idx.find_calls("")))

    def test_import_cycles_terminate(self):
        idx = self.index({"a.py": "from b import run\nrun()", "b.py": "from a import run"})
        self.assertIn("cyclic", idx.find_calls("run")[0]["resolution"]["reason"])

    def test_wildcard_import_does_not_fabricate_a_target(self):
        idx = self.index({"app.py": "def target(): pass\nfrom outside import *\ntarget()"})
        self.assertEqual(idx.find_calls("target")[0]["resolution"]["status"], "unresolved")

    def test_ambiguous_module_roots_are_not_guessed(self):
        idx = self.index({"src/util.py": "def target(): pass", "util.py": "def target(): pass",
                          "app.py": "from util import target\ntarget()"})
        self.assertEqual(idx.find_calls("target")[0]["resolution"]["reason"], "ambiguous module roots")

    def test_long_source_is_capped_and_disclosed(self):
        idx = self.index({"app.py": 'def target():\n    text = "' + 'x'*2000 + '"\n    return text'})
        context = idx.get_symbol_context("app.py", "target", max_chars=100)
        self.assertEqual(len(context["source"]), 100)
        self.assertTrue(context["truncated"])

    def test_snapshot_changes_with_source_not_absolute_directory(self):
        a = self.index({"app.py": "def target(): pass"})
        b = self.index({"app.py": "def target(): pass"})
        c = self.index({"app.py": "def other(): pass"})
        self.assertEqual(a.snapshot_sha256, b.snapshot_sha256)
        self.assertNotEqual(a.snapshot_sha256, c.snapshot_sha256)

    def test_total_byte_budget_is_disclosed(self):
        idx = self.index({"a.py": "x = 1\n", "b.py": "x = 2\n"}, max_total_bytes=7)
        self.assertEqual(len(idx.files), 1)
        self.assertTrue(idx.truncated)

    def test_literal_search_returns_source_citations(self):
        idx = self.index({"app.py": "# literal .* is not a regex\nx = 1"})
        self.assertEqual(idx.search_code(".*")[0]["citation"], "app.py:1")
        with self.assertRaises(ValueError):
            idx.search_code("")

    def test_paths_do_not_trigger_file_reads_or_network_resolution(self):
        idx = self.index({"app.py": "x = 1"})
        for path in ("../app.py", "C:/app.py", "//host/share/app.py", "/app.py"):
            with self.assertRaises(ValueError):
                idx.get_imports(path)

    def test_duplicate_declarations_are_not_silently_selected(self):
        idx = self.index({"app.py": "def target(): pass\ndef target(): pass\ntarget()"})
        with self.assertRaises(ValueError):
            idx.get_symbol_context("app.py", "target")
        self.assertEqual(idx.find_calls("target")[0]["resolution"]["status"], "unresolved")
