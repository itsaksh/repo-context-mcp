"""Interoperability with the optional official MCP SDK; core tests need no SDK."""
import asyncio
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
HAS_SDK = importlib.util.find_spec("mcp") is not None


@unittest.skipUnless(HAS_SDK, "Install .[test] to run official MCP client integration")
class OfficialClientTests(unittest.IsolatedAsyncioTestCase):
    async def connect_and_check(self, mode):
        from mcp import Client
        from mcp.client.stdio import StdioServerParameters
        from jsonschema import validate
        parameters = StdioServerParameters(command=sys.executable,
                                          args=[str(ROOT/"server_entry.py"), str(ROOT/"examples")], cwd=ROOT)
        async with Client(parameters, mode=mode, read_timeout_seconds=10) as client:
            self.assertEqual(client.protocol_version, "2025-11-25")
            tools = (await client.list_tools()).tools
            self.assertEqual(len(tools), 8)
            definitions = {t.name: t for t in tools}
            cases = {
                "repository_summary": {}, "list_symbols": {"query": "invoice"},
                "get_symbol_context": {"path": "sample_app.py", "name": "Checkout.invoice"},
                "get_imports": {"path": "sample_app.py"}, "find_calls": {"query": "total"},
                "search_code": {"query": "Decimal"}, "get_dependencies": {"path": "sample_app.py"},
                "get_callers": {"path": "sample_app.py", "name": "total"},
            }
            for name, arguments in cases.items():
                result = await client.call_tool(name, arguments)
                self.assertFalse(result.is_error, name)
                validate(result.structured_content, definitions[name].output_schema)
                self.assertEqual(json.loads(result.content[0].text), result.structured_content)
            denied = await client.call_tool("get_imports", {"path": "../secret.py"})
            self.assertTrue(denied.is_error)

    async def test_sdk_auto_discovery_falls_back_and_calls_all_tools(self):
        await asyncio.wait_for(self.connect_and_check("auto"), 25)

    async def test_sdk_legacy_handshake_calls_all_tools(self):
        await asyncio.wait_for(self.connect_and_check("legacy"), 25)
