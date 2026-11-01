# Explain Repository Context MCP

## A short introduction

This project gives an AI client small, traceable pieces of a Python repository. Instead of pasting every file into a prompt, a client discovers eight MCP tools and requests symbols, source excerpts, imports, dependencies or supported caller relationships. Every result comes from a read-only source snapshot.

The project was created with AI assistance in November 2026. A candidate should run the examples and make a change they can explain before describing their personal contribution in an interview.

## How the pieces fit

1. `index.py` walks an explicitly chosen directory, applies file and byte limits, reads Python source and builds an in-memory snapshot. It never imports the inspected project.
2. `analysis.py` walks Python AST nodes, records scopes and bindings, and resolves supported lexical declarations and import aliases. It leaves uncertain calls unresolved.
3. `server.py` implements the MCP 2025-11-25 tools capability over newline-delimited JSON-RPC stdio. Input validation, lifecycle handling and structured outputs stay separate from analysis.
4. `tools/demo_client.py` uses the official MCP SDK to discover and call every tool, then records the real outputs in JSON, Markdown and an expandable HTML replay.

## A one minute demo

- Open `evidence/click-demo.html` and identify the repository revision and SDK version.
- Expand `list_symbols` and show the discovered `echo` declaration.
- Expand `get_symbol_context` and show its file citation, source lines and explicit truncation flag.
- Expand `get_dependencies` or `get_callers` and follow one source reference.
- Explain the distinction between supported static references and unresolved runtime behavior.
- Show `evidence/test-results.json` and the successful outside-root rejection.

The HTML file is a saved replay of real MCP calls, not a live AI chat or a recording of an LLM using the tools. The full repository is not included in the project archive.

## Questions to be ready for

**Why use AST rather than text matching for symbols?** AST nodes identify declarations, imports and source locations using Python syntax. Literal search remains useful as a separate tool for finding strings and comments.

**What does static reference mean?** The source binds a name to a declaration or a supported import alias. It does not prove that runtime dispatch, decorators or monkeypatching will call the original implementation.

**Why leave so many calls unresolved?** A parameter such as `handler`, an instance method such as `self.save`, a factory result, an external dependency or ambiguous binding may require runtime information. Guessing would create misleading dependency claims.

**How are relative imports resolved?** The resolver derives a package name from the file path, supports a conventional `src` root, applies the relative import level, and follows uniquely indexed modules. It does not reproduce every import hook or package configuration.

**How are files contained?** Initial indexing checks resolved paths and ignores symlinks. Tool calls look up relative paths only in the snapshot, rejecting absolute paths, drive prefixes and parent traversal. They do not read a new file or resolve a network path.

**Why character limits?** They provide a model-independent, exact bound on excerpt size. They are not token counts; a future tokenizer integration could add model-specific budgets.

**What is actually tested?** Syntax behavior, aliases, re-exports, shadowed names, root containment, truncation, JSON-RPC errors and both automatic and legacy official-SDK connections. The SDK tests call all eight tools and validate output schemas.

## A useful first personal change

Add a fixture with `from ..helpers import function as alias`, predict the expected resolution, and add a test. Then implement and explain a small improvement, such as pagination for symbol results or filtering dependencies to a selected source directory. Keep the change focused and record the actual contribution.

## Resume wording after reviewing and contributing

Repository Context MCP — AI-assisted Python portfolio project, November 2026

- Implemented a read-only MCP interface exposing eight repository-analysis tools with source citations and bounded excerpts.
- Added AST-based symbol extraction and conservative import-alias analysis with explicit unresolved-call reporting.
- Verified all tools through the official MCP Python SDK against a pinned Click checkout containing 91 Python files and 2,078 symbols.

Use the implementation bullets only for work the candidate has reviewed and can explain. Add the actual personally implemented change rather than inventing prior users, deployments or historical results.
