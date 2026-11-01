import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from repocontext.index import RepositoryIndex
from repocontext.server import Server

ROOT = Path(__file__).resolve().parents[1]


class ContextTests(unittest.TestCase):
    def setUp(self):
        self.index = RepositoryIndex(ROOT / "examples")

    def test_qualified_methods_and_async_functions(self):
        names = {s["name"]: s["kind"] for s in self.index.list_symbols()}
        self.assertIn("Checkout.invoice", names)
        self.assertEqual(names["health"], "async_function")

    def test_context_has_original_line_numbers(self):
        result = self.index.get_symbol_context("sample_app.py", "Checkout.invoice")
        self.assertIn("def invoice", result["source"])
        self.assertTrue(result["source"].startswith(f"{result['line']}:"))
        self.assertFalse(result["truncated"])

    def test_imports_and_syntactic_calls(self):
        self.assertEqual(self.index.get_imports("sample_app.py")[0]["module"], "decimal")
        found = self.index.find_calls("total")
        self.assertEqual(found[0]["caller"], "Checkout.invoice")

    def test_traversal_and_unindexed_files_rejected(self):
        for path in ("../repocontext/server.py", "missing.py"):
            with self.assertRaises(ValueError):
                self.index.get_imports(path)

    def test_bad_limits_rejected(self):
        for limit in (True, 0, 101, "3"):
            with self.assertRaises(ValueError):
                self.index.list_symbols(limit=limit)

    def test_invalid_python_is_reported_without_importing_it(self):
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp)
            (p / "bad.py").write_text("def broken(:", encoding="utf-8")
            (p / "never_execute.py").write_text("raise RuntimeError('do not run')", encoding="utf-8")
            idx = RepositoryIndex(p)
            self.assertEqual(idx.summary()["files"], 1)
            self.assertEqual(idx.skipped[0]["reason"], "SyntaxError")

    def test_ignored_directories_and_size_limit(self):
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp)
            (p / ".venv").mkdir()
            (p / ".venv" / "hidden.py").write_text("def hidden(): pass")
            (p / "large.py").write_text("x = 1\n" * 40)
            idx = RepositoryIndex(p, max_file_bytes=30)
            self.assertEqual(idx.summary()["files"], 0)
            self.assertEqual(len(idx.skipped), 1)

    def test_file_limit_is_disclosed(self):
        idx = RepositoryIndex(ROOT / "repocontext", max_files=1)
        self.assertEqual(len(idx.files), 1)
        self.assertTrue(idx.truncated)

    def test_symlink_outside_root_is_not_indexed(self):
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp)
            root = p / "inside"
            root.mkdir()
            outside = p / "outside.py"
            outside.write_text("def secret(): pass")
            try:
                (root / "link.py").symlink_to(outside)
            except (OSError, NotImplementedError):
                self.skipTest("This OS does not permit creating symlinks")
            self.assertEqual(RepositoryIndex(root).summary()["files"], 0)


class ProtocolTests(unittest.TestCase):
    def ready_server(self):
        s = Server(RepositoryIndex(ROOT / "examples"))
        s.dispatch({"jsonrpc": "2.0", "id": 1, "method": "initialize",
                    "params": {"protocolVersion": "2025-11-25"}})
        s.dispatch({"jsonrpc": "2.0", "method": "notifications/initialized"})
        return s

    def test_tools_need_initialization(self):
        s = Server(RepositoryIndex(ROOT / "examples"))
        self.assertIn("error", s.dispatch({"jsonrpc": "2.0", "id": 1, "method": "tools/list"}))

    def test_tool_argument_validation_and_errors(self):
        s = self.ready_server()
        base = {"jsonrpc": "2.0", "id": 2, "method": "tools/call"}
        bad = s.dispatch({**base, "params": {"name": "get_imports", "arguments": {"path": 9}}})
        self.assertEqual(bad["error"]["code"], -32602)
        bad = s.dispatch({**base, "params": {"name": "get_imports", "arguments": {"path": "../outside.py"}}})
        self.assertTrue(bad["result"]["isError"])

    def test_unknown_method_and_tool(self):
        s = self.ready_server()
        self.assertEqual(s.dispatch({"jsonrpc": "2.0", "id": 4, "method": "unknown"})["error"]["code"], -32601)
        self.assertEqual(s.dispatch({"jsonrpc": "2.0", "id": 5, "method": "tools/call", "params": {"name": "write_file"}})["error"]["code"], -32602)

    def test_subprocess_handshake_discovery_and_call(self):
        messages = [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-11-25"}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
            {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "list_symbols", "arguments": {"query": "invoice"}}},
        ]
        run = subprocess.run([sys.executable, "-m", "repocontext", str(ROOT / "examples")],
                             cwd=ROOT, input="\n".join(map(json.dumps, messages))+"\n",
                             capture_output=True, text=True, timeout=15, check=True)
        replies = [json.loads(line) for line in run.stdout.splitlines()]
        self.assertEqual([r["id"] for r in replies], [1, 2, 3])
        self.assertEqual(len(replies[1]["result"]["tools"]), 8)
        payload = replies[2]["result"]["structuredContent"]["data"]
        self.assertEqual(payload[0]["name"], "Checkout.invoice")

    def test_parse_error_does_not_stop_next_message(self):
        run = subprocess.run([sys.executable, "-m", "repocontext", str(ROOT / "examples")],
                             cwd=ROOT, input='not-json\n{"jsonrpc":"2.0","id":2,"method":"ping"}\n',
                             capture_output=True, text=True, timeout=15, check=True)
        replies = [json.loads(line) for line in run.stdout.splitlines()]
        self.assertEqual(replies[0]["error"]["code"], -32700)
        self.assertEqual(replies[1]["result"], {})


if __name__ == "__main__":
    unittest.main()
