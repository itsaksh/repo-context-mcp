"""Exercise all tools through the official MCP client and save a readable replay."""
from __future__ import annotations
import argparse
import asyncio
from datetime import datetime, timezone
import html
import importlib.metadata
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


async def capture(args):
    from mcp import Client
    from mcp.client.stdio import StdioServerParameters
    parameters = StdioServerParameters(command=sys.executable,
                                      args=[str(ROOT/"server_entry.py"), str(args.repository.resolve())], cwd=ROOT)
    events = []
    async with Client(parameters, read_timeout_seconds=15) as client:
        tools = (await client.list_tools()).tools

        async def call(name, arguments):
            result = await client.call_tool(name, arguments)
            if result.is_error:
                raise RuntimeError(f"{name} failed: {result.content}")
            output = result.structured_content["data"]
            events.append({"tool": name, "arguments": arguments, "output": output})
            return output

        summary = await call("repository_summary", {})
        symbols = await call("list_symbols", {"query": args.query, "limit": 100})
        if not symbols:
            raise RuntimeError("No matching symbols; choose another --query")
        symbol = sorted(symbols, key=lambda s: (s["name"] != args.query, not s["path"].startswith("src/"), s["path"]))[0]
        target = {"path": symbol["path"], "name": symbol["name"]}
        await call("get_symbol_context", {**target, "max_chars": 2000})
        await call("get_imports", {"path": symbol["path"]})
        await call("find_calls", {"query": args.query, "limit": 8})
        await call("search_code", {"query": args.query, "limit": 8})
        await call("get_dependencies", {"path": symbol["path"]})
        await call("get_callers", {**target, "limit": 8})
        refused = await client.call_tool("get_imports", {"path": "../outside.py"})
        if not refused.is_error:
            raise RuntimeError("Root containment check failed")
        return {"created_utc": datetime.now(timezone.utc).isoformat(),
                "repository_url": args.repository_url, "repository_revision": args.revision,
                "sdk_version": importlib.metadata.version("mcp"), "protocol_version": client.protocol_version,
                "server_version": client.server_info.version, "tools_discovered": [t.name for t in tools],
                "summary": summary, "selected_symbol": target, "outside_path_rejected": True, "events": events,
                "scope": "This is a client/tool interoperability replay, not an LLM reasoning or accuracy benchmark."}


def write_reports(report, output):
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    summary = report["summary"]
    lines = ["# Repository Context MCP demo", "", f"Repository: {report['repository_url']}",
             f"Revision: `{report['repository_revision']}`", f"Official MCP SDK: {report['sdk_version']}",
             f"Negotiated protocol: {report['protocol_version']}", "", "## Measured index counts", "",
             f"- Python files: {summary['files']}", f"- Symbols: {summary['symbols']}",
             f"- Syntactic call sites: {summary['calls']}", f"- Supported static references: {summary['static_references']}",
             f"- Unresolved call sites: {summary['unresolved_calls']}", f"- Truncated: {summary['truncated']}",
             f"- Outside-root request rejected: {report['outside_path_rejected']}", "",
             "These are inventory counts, not accuracy measurements or runtime call guarantees.", ""]
    for event in report["events"]:
        lines += [f"## {event['tool']}", "", "Arguments", "```json", json.dumps(event["arguments"], indent=2),
                  "```", "", "Result", "```json", json.dumps(event["output"], indent=2, ensure_ascii=False), "```", ""]
    output.with_suffix(".md").write_text("\n".join(lines), encoding="utf-8")
    sections = []
    for event in report["events"]:
        sections.append(f'<details><summary>{html.escape(event["tool"])}</summary><h3>Arguments</h3><pre>{html.escape(json.dumps(event["arguments"], indent=2))}</pre><h3>Result</h3><pre>{html.escape(json.dumps(event["output"], indent=2, ensure_ascii=False))}</pre></details>')
    page = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Repository Context MCP demo</title><style>body{font:16px/1.6 system-ui,sans-serif;max-width:1000px;margin:40px auto;padding:0 24px;color:#182238;background:#f6f8fb}header,details{background:white;padding:24px;margin:16px 0;border:1px solid #d9e0eb;border-radius:12px}h1{margin-top:0;font-size:32px}summary{cursor:pointer;font-weight:700}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f1f4f8;padding:16px;font:13px/1.5 Consolas,monospace}small{color:#526078}a{color:#2457af}</style><header><h1>Repository Context MCP</h1>'''
    page += f'<p>Official SDK client replay on <a href="{html.escape(report["repository_url"], quote=True)}">the analyzed repository</a>.</p><p><b>{summary["files"]}</b> Python files · <b>{summary["symbols"]}</b> symbols · <b>{len(report["tools_discovered"])}</b> tools exercised</p><small>Revision {html.escape(report["repository_revision"])}<br>SDK {html.escape(report["sdk_version"])} · Protocol {html.escape(report["protocol_version"])}</small><p>Inventory counts are not accuracy scores. This demo executes tools through MCP; it does not run an LLM.</p></header>'
    page += "".join(sections)+"</html>"
    output.with_suffix(".html").write_text(page, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", type=Path)
    parser.add_argument("--query", default="echo")
    parser.add_argument("--repository-url", default="local repository")
    parser.add_argument("--revision", default="unversioned")
    parser.add_argument("--output", type=Path, default=ROOT/"evidence"/"demo.json")
    args = parser.parse_args()
    report = asyncio.run(capture(args))
    write_reports(report, args.output)
    print(json.dumps({"output": str(args.output), "summary": report["summary"],
                      "tools_exercised": len(report["events"])}, indent=2))


if __name__ == "__main__":
    main()
