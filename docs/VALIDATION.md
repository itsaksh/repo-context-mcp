# Verification record

Verified on Windows with Python 3.12.14 on 1 November 2026.

- 37 automated tests: 36 passed, one symlink-creation test skipped because this Windows session does not permit creating symlinks.
- Official MCP Python SDK 2.3.0 connected through stdio in automatic and legacy modes. Both negotiated protocol 2025-11-25.
- All eight tools were called through the official client; their structured outputs were checked against their advertised JSON schemas.
- A separate SDK replay analyzed pallets/click revision `2247b35ea1c47c727d7a06e51fa280e12a863ff6`.
- The Click snapshot contained 91 Python files, 2,078 symbols and 7,084 syntactic call sites. The resolver produced 1,984 supported static references and left 5,100 call sites unresolved. No files were skipped and the snapshot was not truncated.
- A request outside the selected root was rejected.
- A pure-Python wheel was built, installed into an isolated local target, and its module entry point was run successfully from outside the source directory.

These are inventory and interoperability results, not an accuracy benchmark, runtime call graph or production readiness claim. The Click checkout includes its examples and tests. Its code was parsed, not imported or executed.

The first SDK run stalled inside a restricted Windows sandbox. The same tests passed with normal Windows subprocess permissions. The passing results use that environment. No GUI host, OpenCode integration or LLM-driven agent session has been tested.

GitHub Actions is configured for Python 3.11, 3.12 and 3.13, including installation of the official SDK test extra. The hosted workflow has not run because publishing is deferred.
