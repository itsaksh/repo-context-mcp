# Repository Context MCP

Read-only Python repository analysis for AI clients. Eight MCP tools expose symbols, cited source excerpts, import dependencies and supported static caller relationships. The inspected code is parsed with Python AST and never imported or executed.

Version 0.2.0 was created with AI assistance as a portfolio project in November 2026. Its scope and verification results are explicit: this is a working developer-tool prototype, not a production deployment or a complete runtime call graph.

## See it work

Open [the expandable Click demo](evidence/click-demo.html). It replays real tool calls made by the official MCP Python SDK against a pinned public repository. Machine-readable results are in [click-demo.json](evidence/click-demo.json).

| Verified item | Result |
| --- | --- |
| Automated tests | 36 passed, one Windows symlink test skipped |
| Official client | MCP Python SDK 2.3.0, automatic and legacy connection modes |
| Negotiated protocol | 2025-11-25 over stdio |
| Tools exercised through SDK | All eight |
| Public repository | pallets/click at `2247b35ea1c47c727d7a06e51fa280e12a863ff6` |
| Parsed inventory | 91 Python files, 2,078 symbols, no truncation or skipped files |

The inventory includes Click's examples and tests. Counts are not accuracy measurements. No LLM session, GUI host or OpenCode integration has been tested. See [the verification record](docs/VALIDATION.md).

## Quick start

Python 3.11 or newer. The server has no third-party runtime dependencies. From this project directory:

```sh
python -m repocontext examples --summary
python -m repocontext /absolute/path/to/a/python/repository
```

The second command waits for MCP messages on stdin; it is not an interactive chat prompt. `server_entry.py` is an alternative absolute-path entry point that works from another working directory.

Install the optional test/client dependencies in a project environment:

```sh
python -m venv .venv
# Activate .venv with your shell's normal activation command.
python -m pip install ".[test]"
python -m unittest discover -s tests -v
```

Without the test extra, the core tests run and official-client tests are skipped. Full local verification used normal Windows subprocess permissions; a restricted process sandbox stalled the SDK's stdio connection.

## Tools

| Tool | Purpose |
| --- | --- |
| `repository_summary` | Inventory, limits, skipped files and stable snapshot hash |
| `list_symbols` | Classes, functions and async functions with qualified names and line citations |
| `get_symbol_context` | Source excerpt, file hash and explicit character/line truncation |
| `get_imports` | Import evidence and uniquely indexed module paths |
| `find_calls` | Syntactic calls, supported static targets and unresolved reasons |
| `search_code` | Literal source search with line citations |
| `get_dependencies` | Indexed dependencies supported by import statements |
| `get_callers` | Callers found through supported lexical and import-alias analysis |

Successful results include `structuredContent: {"data": ...}` and matching JSON text. Each tool advertises input and output schemas. Invalid protocol arguments use JSON-RPC errors; a valid request for an unavailable symbol/path returns a tool error.

## Connect an MCP host

Generate a configuration using the interpreter you intend the host to run:

```sh
python tools/write_mcp_config.py /absolute/path/to/repository
```

This prints a conventional `mcpServers` configuration with absolute interpreter, entry-point and repository paths. It does not modify host settings. Host configuration formats may differ. The verified integration is the official Python SDK client.

## Reproduce the public repository demo

The Click checkout is not shipped in this project. With Git and the test extra installed:

```sh
git clone https://github.com/pallets/click.git ../click-demo
git -C ../click-demo checkout 2247b35ea1c47c727d7a06e51fa280e12a863ff6
python tools/demo_client.py ../click-demo --query echo --repository-url https://github.com/pallets/click --revision 2247b35ea1c47c727d7a06e51fa280e12a863ff6 --output evidence/click-demo.json
```

The client discovers all tools, fetches a real declaration, inspects its callers and imports, and checks rejection of an outside-root path. It writes JSON, Markdown and HTML. This is a tool replay, not an LLM reasoning evaluation. A source snapshot hash helps identify the exact analyzed content.

## Design and practical limits

- Supports lexical declarations, import aliases, relative imports, conventional `src` roots and simple re-exports. Ambiguous modules, rebound names, parameters and wildcard imports remain unresolved.
- Static references do not establish runtime dispatch. Instance types, inheritance, monkeypatches, decorator behavior, `exec`, custom import hooks and arbitrary module roots are not modeled. Comprehension bindings are treated conservatively in the enclosing analysis scope.
- A snapshot is built at startup. Restart to see changed source. Duplicate qualified declarations cannot be selected silently.
- Defaults: 500 successfully indexed Python files, 256 KiB per file and 16 MiB total source. Truncation and skipped files are reported. Symlinks and resolved out-of-root directories are excluded during the walk.
- Tool paths are looked up only in the snapshot. Parent traversal, absolute paths and drive prefixes are rejected without new filesystem or network reads.
- Source excerpts are capped at 120 lines and a configurable character budget. Characters are not model tokens.
- Indexing does not interpret repository text as instructions. The consuming AI client must handle untrusted source appropriately.
- Only MCP tools over sequential stdio are implemented. No HTTP server, sampling, resources, live reindexing or cancellation protocol is claimed.
- The fixed ignored-directory policy does not implement arbitrary `.gitignore` patterns. Dependencies outside the snapshot remain unresolved.

## Learn and present it

[The explanation guide](docs/EXPLAIN_THE_PROJECT.md) includes an architecture walkthrough, a one-minute demo route, interview questions and a suggested first personal change. Resume wording should describe actual reviewed work and the candidate's contribution.

Original project code is available under the [MIT license](LICENSE). Click excerpts in the demo are covered by [the included Click license](evidence/CLICK_LICENSE.txt). Click and the MCP SDK projects do not endorse this portfolio project.

References: [MCP lifecycle](https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle), [stdio transport](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports), [tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools), [official SDK client](https://py.sdk.modelcontextprotocol.io/client/), and [Python AST](https://docs.python.org/3/library/ast.html).
