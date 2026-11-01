# Repository Context MCP demo

Repository: https://github.com/pallets/click
Revision: `2247b35ea1c47c727d7a06e51fa280e12a863ff6`
Official MCP SDK: 2.3.0
Negotiated protocol: 2025-11-25

## Measured index counts

- Python files: 91
- Symbols: 2078
- Syntactic call sites: 7084
- Supported static references: 1984
- Unresolved call sites: 5100
- Truncated: False
- Outside-root request rejected: True

These are inventory counts, not accuracy measurements or runtime call guarantees.

## repository_summary

Arguments
```json
{}
```

Result
```json
{
  "files": 91,
  "symbols": 2078,
  "calls": 7084,
  "static_references": 1984,
  "unresolved_calls": 5100,
  "skipped": [],
  "truncated": false,
  "indexed_utf8_bytes": 1003633,
  "limits": {
    "max_files": 500,
    "max_file_bytes": 262144,
    "max_total_bytes": 16777216
  },
  "snapshot_sha256": "4f4415befc79d59be2c0e75b265d3f3124cfec4e3fcdfdcb03c804c4ee9bc9c6",
  "call_resolution": "Conservative static references, not runtime guarantees. Instance dispatch remains unresolved."
}
```

## list_symbols

Arguments
```json
{
  "query": "echo",
  "limit": 100
}
```

Result
```json
[
  {
    "path": "src/click/core.py",
    "name": "_echo_aborted",
    "kind": "function",
    "line": 103,
    "definition_line": 103,
    "end_line": 105,
    "signature": "_echo_aborted()",
    "docstring": "Write the final abort message to standard error.",
    "citation": "src/click/core.py:103"
  },
  {
    "path": "src/click/termui.py",
    "name": "echo_via_pager",
    "kind": "function",
    "line": 367,
    "definition_line": 367,
    "end_line": 399,
    "signature": "echo_via_pager(text_or_generator: cabc.Iterable[str] | t.Callable[[], cabc.Iterable[str]] | str, color: bool | None=None)",
    "docstring": "This function takes a text and shows it via an environment specific\npager on stdout.\n\n.. versionchanged:: 3.0\n   Added the `color` flag.\n\n:param text_or_generator: the text to page, or alternatively, a\n                          generator emitting the text to page.\n:param color: controls if the pager supports ANSI colors or not.  The\n              default is autodetection.",
    "citation": "src/click/termui.py:367"
  },
  {
    "path": "src/click/termui.py",
    "name": "secho",
    "kind": "function",
    "line": 780,
    "definition_line": 780,
    "end_line": 811,
    "signature": "secho(message: t.Any | None=None, file: t.IO[t.AnyStr] | None=None, nl: bool=True, err: bool=False, color: bool | None=None, **styles: t.Any)",
    "docstring": "This function combines :func:`echo` and :func:`style` into one\ncall.  As such the following two calls are the same::\n\n    click.secho('Hello World!', fg='green')\n    click.echo(click.style('Hello World!', fg='green'))\n\nAll keyword arguments are forwarded to the underlying functions\ndepending on which one they go with.\n\nNon-string types will be converted to :class:`str`. However,\n:class:`bytes` are passed directly to :meth:`echo` without applying\nstyle. If you want to style bytes that represent text, call\n:meth:`bytes.decode` first.\n\n.. versionchanged:: 8.0\n    A non-string ``message`` is converted to a string. Bytes are\n    passed through without style applied.\n\n.. versionadded:: 2.0",
    "citation": "src/click/termui.py:780"
  },
  {
    "path": "src/click/testing.py",
    "name": "EchoingStdin",
    "kind": "class",
    "line": 32,
    "definition_line": 32,
    "end_line": 67,
    "signature": "EchoingStdin",
    "docstring": "",
    "citation": "src/click/testing.py:32"
  },
  {
    "path": "src/click/testing.py",
    "name": "EchoingStdin.__init__",
    "kind": "function",
    "line": 37,
    "definition_line": 37,
    "end_line": 40,
    "signature": "__init__(self, input: t.BinaryIO, output: t.BinaryIO)",
    "docstring": "",
    "citation": "src/click/testing.py:37"
  },
  {
    "path": "src/click/testing.py",
    "name": "EchoingStdin.__getattr__",
    "kind": "function",
    "line": 42,
    "definition_line": 42,
    "end_line": 43,
    "signature": "__getattr__(self, x: str)",
    "docstring": "",
    "citation": "src/click/testing.py:42"
  },
  {
    "path": "src/click/testing.py",
    "name": "EchoingStdin._echo",
    "kind": "function",
    "line": 45,
    "definition_line": 45,
    "end_line": 49,
    "signature": "_echo(self, rv: bytes)",
    "docstring": "",
    "citation": "src/click/testing.py:45"
  },
  {
    "path": "src/click/testing.py",
    "name": "EchoingStdin.read",
    "kind": "function",
    "line": 51,
    "definition_line": 51,
    "end_line": 52,
    "signature": "read(self, n: int=-1)",
    "docstring": "",
    "citation": "src/click/testing.py:51"
  },
  {
    "path": "src/click/testing.py",
    "name": "EchoingStdin.read1",
    "kind": "function",
    "line": 54,
    "definition_line": 54,
    "end_line": 55,
    "signature": "read1(self, n: int=-1)",
    "docstring": "",
    "citation": "src/click/testing.py:54"
  },
  {
    "path": "src/click/testing.py",
    "name": "EchoingStdin.readline",
    "kind": "function",
    "line": 57,
    "definition_line": 57,
    "end_line": 58,
    "signature": "readline(self, n: int=-1)",
    "docstring": "",
    "citation": "src/click/testing.py:57"
  },
  {
    "path": "src/click/testing.py",
    "name": "EchoingStdin.readlines",
    "kind": "function",
    "line": 60,
    "definition_line": 60,
    "end_line": 61,
    "signature": "readlines(self)",
    "docstring": "",
    "citation": "src/click/testing.py:60"
  },
  {
    "path": "src/click/testing.py",
    "name": "EchoingStdin.__iter__",
    "kind": "function",
    "line": 63,
    "definition_line": 63,
    "end_line": 64,
    "signature": "__iter__(self)",
    "docstring": "",
    "citation": "src/click/testing.py:63"
  },
  {
    "path": "src/click/testing.py",
    "name": "EchoingStdin.__repr__",
    "kind": "function",
    "line": 66,
    "definition_line": 66,
    "end_line": 67,
    "signature": "__repr__(self)",
    "docstring": "",
    "citation": "src/click/testing.py:66"
  },
  {
    "path": "src/click/testing.py",
    "name": "_pause_echo",
    "kind": "function",
    "line": 70,
    "definition_line": 71,
    "end_line": 77,
    "signature": "_pause_echo(stream: EchoingStdin | None)",
    "docstring": "",
    "citation": "src/click/testing.py:71"
  },
  {
    "path": "src/click/utils.py",
    "name": "echo",
    "kind": "function",
    "line": 240,
    "definition_line": 240,
    "end_line": 334,
    "signature": "echo(message: object=None, file: t.IO[t.Any] | None=None, nl: bool=True, err: bool=False, color: bool | None=None)",
    "docstring": "Print a message and newline to stdout or a file. This should be\nused instead of :func:`print` because it provides better support\nfor different data, files, and environments.\n\nCompared to :func:`print`, this does the following:\n\n-   Ensures that the output encoding is not misconfigured on Linux.\n-   Supports Unicode in the Windows console.\n-   Supports writing to binary outputs, and supports writing bytes\n    to text outputs.\n-   Removes ANSI color and style codes if the output does not look\n    like an interactive terminal.\n-   Always flushes the output.\n\n:param message: The string or bytes to output. Other objects are\n    converted to strings.\n:param file: The file to write to. Defaults to ``stdout``.\n:param err: Write to ``stderr`` instead of ``stdout``.\n:param nl: Print a newline after ",
    "citation": "src/click/utils.py:240"
  },
  {
    "path": "tests/test_termui.py",
    "name": "test_secho",
    "kind": "function",
    "line": 295,
    "definition_line": 295,
    "end_line": 299,
    "signature": "test_secho(runner)",
    "docstring": "",
    "citation": "tests/test_termui.py:295"
  },
  {
    "path": "tests/test_termui.py",
    "name": "test_secho_non_text",
    "kind": "function",
    "line": 302,
    "definition_line": 306,
    "end_line": 310,
    "signature": "test_secho_non_text(runner, value, expect)",
    "docstring": "",
    "citation": "tests/test_termui.py:306"
  },
  {
    "path": "tests/test_termui.py",
    "name": "test_echo_via_pager_real_pager_handles_ansi",
    "kind": "function",
    "line": 752,
    "definition_line": 763,
    "end_line": 774,
    "signature": "test_echo_via_pager_real_pager_handles_ansi(monkeypatch, capfd, color, expected)",
    "docstring": "``echo_via_pager`` should honor ``color`` like ``get_pager_file``.",
    "citation": "tests/test_termui.py:763"
  },
  {
    "path": "tests/test_termui.py",
    "name": "test_echo_via_pager_streams_each_write",
    "kind": "function",
    "line": 928,
    "definition_line": 928,
    "end_line": 963,
    "signature": "test_echo_via_pager_streams_each_write(monkeypatch)",
    "docstring": "Each write is flushed so a slow generator streams to the pager\nincrementally instead of buffering until the end (issues #3242, #2542).",
    "citation": "tests/test_termui.py:928"
  },
  {
    "path": "tests/test_termui.py",
    "name": "test_echo_via_pager_streams_each_write.RecordingStream",
    "kind": "class",
    "line": 934,
    "definition_line": 934,
    "end_line": 944,
    "signature": "RecordingStream",
    "docstring": "",
    "citation": "tests/test_termui.py:934"
  },
  {
    "path": "tests/test_termui.py",
    "name": "test_echo_via_pager_streams_each_write.RecordingStream.__init__",
    "kind": "function",
    "line": 935,
    "definition_line": 935,
    "end_line": 937,
    "signature": "__init__(self)",
    "docstring": "",
    "citation": "tests/test_termui.py:935"
  },
  {
    "path": "tests/test_termui.py",
    "name": "test_echo_via_pager_streams_each_write.RecordingStream.write",
    "kind": "function",
    "line": 939,
    "definition_line": 939,
    "end_line": 941,
    "signature": "write(self, s)",
    "docstring": "",
    "citation": "tests/test_termui.py:939"
  },
  {
    "path": "tests/test_termui.py",
    "name": "test_echo_via_pager_streams_each_write.RecordingStream.flush",
    "kind": "function",
    "line": 943,
    "definition_line": 943,
    "end_line": 944,
    "signature": "flush(self)",
    "docstring": "",
    "citation": "tests/test_termui.py:943"
  },
  {
    "path": "tests/test_termui.py",
    "name": "test_echo_via_pager_streams_each_write.generate",
    "kind": "function",
    "line": 950,
    "definition_line": 950,
    "end_line": 953,
    "signature": "generate()",
    "docstring": "",
    "citation": "tests/test_termui.py:950"
  },
  {
    "path": "tests/test_termui.py",
    "name": "test_echo_via_pager_tty_pager_missing",
    "kind": "function",
    "line": 1040,
    "definition_line": 1040,
    "end_line": 1060,
    "signature": "test_echo_via_pager_tty_pager_missing(runner, monkeypatch)",
    "docstring": "``echo_via_pager`` through the tty fallback keeps ``CliRunner`` working.\n\nRegression for issue #3449 via the pager fallback: a tty with ``PAGER``\npointing at a missing binary used to close the runner's stdout, breaking\n``CliRunner.invoke``.",
    "citation": "tests/test_termui.py:1040"
  },
  {
    "path": "tests/test_termui.py",
    "name": "test_echo_via_pager_tty_pager_missing.cli",
    "kind": "function",
    "line": 1054,
    "definition_line": 1055,
    "end_line": 1056,
    "signature": "cli()",
    "docstring": "",
    "citation": "tests/test_termui.py:1055"
  },
  {
    "path": "tests/test_termui.py",
    "name": "_page_with_echo_via_pager",
    "kind": "function",
    "line": 1194,
    "definition_line": 1194,
    "end_line": 1195,
    "signature": "_page_with_echo_via_pager()",
    "docstring": "",
    "citation": "tests/test_termui.py:1194"
  },
  {
    "path": "tests/test_testing.py",
    "name": "test_echo_stdin_stream",
    "kind": "function",
    "line": 34,
    "definition_line": 34,
    "end_line": 49,
    "signature": "test_echo_stdin_stream()",
    "docstring": "",
    "citation": "tests/test_testing.py:34"
  },
  {
    "path": "tests/test_testing.py",
    "name": "test_echo_stdin_stream.test",
    "kind": "function",
    "line": 35,
    "definition_line": 36,
    "end_line": 44,
    "signature": "test()",
    "docstring": "",
    "citation": "tests/test_testing.py:36"
  },
  {
    "path": "tests/test_testing.py",
    "name": "test_echo_stdin_prompts",
    "kind": "function",
    "line": 52,
    "definition_line": 52,
    "end_line": 89,
    "signature": "test_echo_stdin_prompts()",
    "docstring": "",
    "citation": "tests/test_testing.py:52"
  },
  {
    "path": "tests/test_testing.py",
    "name": "test_echo_stdin_prompts.test_python_input",
    "kind": "function",
    "line": 53,
    "definition_line": 54,
    "end_line": 56,
    "signature": "test_python_input()",
    "docstring": "",
    "citation": "tests/test_testing.py:54"
  },
  {
    "path": "tests/test_testing.py",
    "name": "test_echo_stdin_prompts.test_prompt",
    "kind": "function",
    "line": 63,
    "definition_line": 65,
    "end_line": 66,
    "signature": "test_prompt(foo)",
    "docstring": "",
    "citation": "tests/test_testing.py:65"
  },
  {
    "path": "tests/test_testing.py",
    "name": "test_echo_stdin_prompts.test_hidden_prompt",
    "kind": "function",
    "line": 72,
    "definition_line": 74,
    "end_line": 75,
    "signature": "test_hidden_prompt(foo)",
    "docstring": "",
    "citation": "tests/test_testing.py:74"
  },
  {
    "path": "tests/test_testing.py",
    "name": "test_echo_stdin_prompts.test_multiple_prompts",
    "kind": "function",
    "line": 81,
    "definition_line": 84,
    "end_line": 85,
    "signature": "test_multiple_prompts(foo, bar)",
    "docstring": "",
    "citation": "tests/test_testing.py:84"
  },
  {
    "path": "tests/test_testing.py",
    "name": "test_getchar.getchar_echo",
    "kind": "function",
    "line": 152,
    "definition_line": 153,
    "end_line": 154,
    "signature": "getchar_echo()",
    "docstring": "",
    "citation": "tests/test_testing.py:153"
  },
  {
    "path": "tests/test_testing.py",
    "name": "test_with_echo_via_pager",
    "kind": "function",
    "line": 260,
    "definition_line": 260,
    "end_line": 268,
    "signature": "test_with_echo_via_pager()",
    "docstring": "",
    "citation": "tests/test_testing.py:260"
  },
  {
    "path": "tests/test_testing.py",
    "name": "test_with_echo_via_pager.cli",
    "kind": "function",
    "line": 261,
    "definition_line": 262,
    "end_line": 263,
    "signature": "cli()",
    "docstring": "",
    "citation": "tests/test_testing.py:262"
  },
  {
    "path": "tests/test_utils/test_echo.py",
    "name": "test_echo",
    "kind": "function",
    "line": 12,
    "definition_line": 12,
    "end_line": 33,
    "signature": "test_echo(runner)",
    "docstring": "",
    "citation": "tests/test_utils/test_echo.py:12"
  },
  {
    "path": "tests/test_utils/test_echo.py",
    "name": "test_echo.cli",
    "kind": "function",
    "line": 23,
    "definition_line": 24,
    "end_line": 25,
    "signature": "cli()",
    "docstring": "",
    "citation": "tests/test_utils/test_echo.py:24"
  },
  {
    "path": "tests/test_utils/test_echo.py",
    "name": "test_echo_custom_file",
    "kind": "function",
    "line": 36,
    "definition_line": 36,
    "end_line": 43,
    "signature": "test_echo_custom_file()",
    "docstring": "",
    "citation": "tests/test_utils/test_echo.py:36"
  },
  {
    "path": "tests/test_utils/test_echo.py",
    "name": "test_echo_no_streams",
    "kind": "function",
    "line": 46,
    "definition_line": 46,
    "end_line": 52,
    "signature": "test_echo_no_streams(monkeypatch, runner)",
    "docstring": "echo should not fail when stdout and stderr are None with pythonw on Windows.",
    "citation": "tests/test_utils/test_echo.py:46"
  },
  {
    "path": "tests/test_utils/test_echo.py",
    "name": "test_echo_with_capsys",
    "kind": "function",
    "line": 55,
    "definition_line": 55,
    "end_line": 58,
    "signature": "test_echo_with_capsys(capsys)",
    "docstring": "",
    "citation": "tests/test_utils/test_echo.py:55"
  },
  {
    "path": "tests/test_utils/test_echo.py",
    "name": "test_echo_color_flag",
    "kind": "function",
    "line": 61,
    "definition_line": 61,
    "end_line": 88,
    "signature": "test_echo_color_flag(monkeypatch, capfd)",
    "docstring": "",
    "citation": "tests/test_utils/test_echo.py:61"
  },
  {
    "path": "tests/test_utils/test_echo.py",
    "name": "test_echo_writing_to_standard_error",
    "kind": "function",
    "line": 91,
    "definition_line": 92,
    "end_line": 172,
    "signature": "test_echo_writing_to_standard_error(capfd, monkeypatch)",
    "docstring": "",
    "citation": "tests/test_utils/test_echo.py:92"
  },
  {
    "path": "tests/test_utils/test_echo.py",
    "name": "test_echo_writing_to_standard_error.emulate_input",
    "kind": "function",
    "line": 93,
    "definition_line": 93,
    "end_line": 95,
    "signature": "emulate_input(text)",
    "docstring": "Emulate keyboard input.",
    "citation": "tests/test_utils/test_echo.py:93"
  },
  {
    "path": "tests/test_utils/test_echo_via_pager.py",
    "name": "_test_gen_func_echo",
    "kind": "function",
    "line": 44,
    "definition_line": 44,
    "end_line": 47,
    "signature": "_test_gen_func_echo(file=None)",
    "docstring": "",
    "citation": "tests/test_utils/test_echo_via_pager.py:44"
  },
  {
    "path": "tests/test_utils/test_echo_via_pager.py",
    "name": "test_echo_via_pager",
    "kind": "function",
    "line": 55,
    "definition_line": 155,
    "end_line": 190,
    "signature": "test_echo_via_pager(monkeypatch, capfd, pager_cmd, test, tmp_path)",
    "docstring": "",
    "citation": "tests/test_utils/test_echo_via_pager.py:155"
  },
  {
    "path": "tests/test_utils/test_echo_via_pager.py",
    "name": "test_echo_via_pager_yields_before_exception",
    "kind": "function",
    "line": 193,
    "definition_line": 194,
    "end_line": 225,
    "signature": "test_echo_via_pager_yields_before_exception(monkeypatch, tmp_path)",
    "docstring": "A generator that yields then raises: click writes the partial output to\nthe pager stream before propagating the exception.\n\nThe pager file content is intentionally NOT asserted: pipe-drain timing\nbetween click and the pager subprocess is outside click's control\n(#2899, #3470). Spying on ``_PagerWriter.write`` records what click sent\nto the pager, which is deterministic regardless of scheduling.",
    "citation": "tests/test_utils/test_echo_via_pager.py:194"
  },
  {
    "path": "tests/test_utils/test_echo_via_pager.py",
    "name": "test_echo_via_pager_yields_before_exception.spy",
    "kind": "function",
    "line": 209,
    "definition_line": 209,
    "end_line": 211,
    "signature": "spy(self, text)",
    "docstring": "",
    "citation": "tests/test_utils/test_echo_via_pager.py:209"
  },
  {
    "path": "tests/test_utils/test_echo_via_pager.py",
    "name": "test_stress_echo_via_pager_exception_cleanup",
    "kind": "function",
    "line": 228,
    "definition_line": 231,
    "end_line": 259,
    "signature": "test_stress_echo_via_pager_exception_cleanup(_, monkeypatch, tmp_path)",
    "docstring": "Repeated exceptions during ``echo_via_pager`` must not leak subprocesses.\n\nRegression coverage for the cleanup path in ``_pipepager``'s exception\nhandler (issue #2899, PR #3470). Each iteration spawns a real pager\nsubprocess, raises before any data is written and check there is no leak.",
    "citation": "tests/test_utils/test_echo_via_pager.py:231"
  },
  {
    "path": "tests/test_utils/test_echo_via_pager.py",
    "name": "test_stress_echo_via_pager_exception_cleanup.tracking_popen",
    "kind": "function",
    "line": 244,
    "definition_line": 244,
    "end_line": 247,
    "signature": "tracking_popen(*args, **kwargs)",
    "docstring": "",
    "citation": "tests/test_utils/test_echo_via_pager.py:244"
  },
  {
    "path": "tests/test_utils/test_prompt.py",
    "name": "test_prompts_eof.echo",
    "kind": "function",
    "line": 93,
    "definition_line": 94,
    "end_line": 96,
    "signature": "echo()",
    "docstring": "",
    "citation": "tests/test_utils/test_prompt.py:94"
  }
]
```

## get_symbol_context

Arguments
```json
{
  "path": "src/click/utils.py",
  "name": "echo",
  "max_chars": 2000
}
```

Result
```json
{
  "path": "src/click/utils.py",
  "name": "echo",
  "kind": "function",
  "line": 240,
  "definition_line": 240,
  "end_line": 334,
  "signature": "echo(message: object=None, file: t.IO[t.Any] | None=None, nl: bool=True, err: bool=False, color: bool | None=None)",
  "docstring": "Print a message and newline to stdout or a file. This should be\nused instead of :func:`print` because it provides better support\nfor different data, files, and environments.\n\nCompared to :func:`print`, this does the following:\n\n-   Ensures that the output encoding is not misconfigured on Linux.\n-   Supports Unicode in the Windows console.\n-   Supports writing to binary outputs, and supports writing bytes\n    to text outputs.\n-   Removes ANSI color and style codes if the output does not look\n    like an interactive terminal.\n-   Always flushes the output.\n\n:param message: The string or bytes to output. Other objects are\n    converted to strings.\n:param file: The file to write to. Defaults to ``stdout``.\n:param err: Write to ``stderr`` instead of ``stdout``.\n:param nl: Print a newline after ",
  "excerpt_end_line": 286,
  "truncated": true,
  "source": "240: def echo(\n241:     message: object = None,\n242:     file: t.IO[t.Any] | None = None,\n243:     nl: bool = True,\n244:     err: bool = False,\n245:     color: bool | None = None,\n246: ) -> None:\n247:     \"\"\"Print a message and newline to stdout or a file. This should be\n248:     used instead of :func:`print` because it provides better support\n249:     for different data, files, and environments.\n250: \n251:     Compared to :func:`print`, this does the following:\n252: \n253:     -   Ensures that the output encoding is not misconfigured on Linux.\n254:     -   Supports Unicode in the Windows console.\n255:     -   Supports writing to binary outputs, and supports writing bytes\n256:         to text outputs.\n257:     -   Removes ANSI color and style codes if the output does not look\n258:         like an interactive terminal.\n259:     -   Always flushes the output.\n260: \n261:     :param message: The string or bytes to output. Other objects are\n262:         converted to strings.\n263:     :param file: The file to write to. Defaults to ``stdout``.\n264:     :param err: Write to ``stderr`` instead of ``stdout``.\n265:     :param nl: Print a newline after the message. Enabled by default.\n266:     :param color: Force showing or hiding colors and other styles. By\n267:         default Click will remove color if the output does not look like\n268:         an interactive terminal.\n269: \n270:     .. versionchanged:: 8.5.0\n271:         Colorama is no longer used for color on Windows.\n272: \n273:     .. versionchanged:: 6.0\n274:         Support Unicode output on the Windows console. Click does not\n275:         modify ``sys.stdout``, so ``sys.stdout.write()`` and ``print()``\n276:         will still not support Unicode.\n277: \n278:     .. versionchanged:: 4.0\n279:         Added the ``color`` parameter.\n280: \n281:     .. versionadded:: 3.0\n282:         Added the ``err`` parameter.\n283: \n284:     .. versionchanged:: 2.0\n285:         Support colors on Windows if colorama is installed.\n286:     \"\"\"",
  "source_characters": 2000,
  "max_characters": 2000,
  "citation": "src/click/utils.py:240",
  "file_sha256": "4720e22c292047ff1a747546b1ba80e96d1d8e8158e2e21ff01cdddb6498db17"
}
```

## get_imports

Arguments
```json
{
  "path": "src/click/utils.py"
}
```

Result
```json
[
  {
    "module": "__future__",
    "level": 0,
    "member": "annotations",
    "alias": null,
    "line": 1,
    "scope": "",
    "absolute_module": "__future__",
    "indexed_paths": [],
    "citation": "src/click/utils.py:1"
  },
  {
    "module": "collections.abc",
    "alias": "cabc",
    "line": 3,
    "scope": "",
    "level": 0,
    "member": null,
    "absolute_module": "collections.abc",
    "indexed_paths": [],
    "citation": "src/click/utils.py:3"
  },
  {
    "module": "os",
    "alias": null,
    "line": 4,
    "scope": "",
    "level": 0,
    "member": null,
    "absolute_module": "os",
    "indexed_paths": [],
    "citation": "src/click/utils.py:4"
  },
  {
    "module": "re",
    "alias": null,
    "line": 5,
    "scope": "",
    "level": 0,
    "member": null,
    "absolute_module": "re",
    "indexed_paths": [],
    "citation": "src/click/utils.py:5"
  },
  {
    "module": "sys",
    "alias": null,
    "line": 6,
    "scope": "",
    "level": 0,
    "member": null,
    "absolute_module": "sys",
    "indexed_paths": [],
    "citation": "src/click/utils.py:6"
  },
  {
    "module": "typing",
    "alias": "t",
    "line": 7,
    "scope": "",
    "level": 0,
    "member": null,
    "absolute_module": "typing",
    "indexed_paths": [],
    "citation": "src/click/utils.py:7"
  },
  {
    "module": "functools",
    "level": 0,
    "member": "update_wrapper",
    "alias": null,
    "line": 8,
    "scope": "",
    "absolute_module": "functools",
    "indexed_paths": [],
    "citation": "src/click/utils.py:8"
  },
  {
    "module": "gettext",
    "level": 0,
    "member": "gettext",
    "alias": "_",
    "line": 9,
    "scope": "",
    "absolute_module": "gettext",
    "indexed_paths": [],
    "citation": "src/click/utils.py:9"
  },
  {
    "module": "types",
    "level": 0,
    "member": "ModuleType",
    "alias": null,
    "line": 10,
    "scope": "",
    "absolute_module": "types",
    "indexed_paths": [],
    "citation": "src/click/utils.py:10"
  },
  {
    "module": "types",
    "level": 0,
    "member": "TracebackType",
    "alias": null,
    "line": 11,
    "scope": "",
    "absolute_module": "types",
    "indexed_paths": [],
    "citation": "src/click/utils.py:11"
  },
  {
    "module": "_compat",
    "level": 1,
    "member": "_default_text_stderr",
    "alias": null,
    "line": 13,
    "scope": "",
    "absolute_module": "click._compat",
    "indexed_paths": [
      "src/click/_compat.py"
    ],
    "citation": "src/click/utils.py:13"
  },
  {
    "module": "_compat",
    "level": 1,
    "member": "_default_text_stdout",
    "alias": null,
    "line": 14,
    "scope": "",
    "absolute_module": "click._compat",
    "indexed_paths": [
      "src/click/_compat.py"
    ],
    "citation": "src/click/utils.py:14"
  },
  {
    "module": "_compat",
    "level": 1,
    "member": "_find_binary_writer",
    "alias": null,
    "line": 15,
    "scope": "",
    "absolute_module": "click._compat",
    "indexed_paths": [
      "src/click/_compat.py"
    ],
    "citation": "src/click/utils.py:15"
  },
  {
    "module": "_compat",
    "level": 1,
    "member": "binary_streams",
    "alias": null,
    "line": 16,
    "scope": "",
    "absolute_module": "click._compat",
    "indexed_paths": [
      "src/click/_compat.py"
    ],
    "citation": "src/click/utils.py:16"
  },
  {
    "module": "_compat",
    "level": 1,
    "member": "open_stream",
    "alias": null,
    "line": 17,
    "scope": "",
    "absolute_module": "click._compat",
    "indexed_paths": [
      "src/click/_compat.py"
    ],
    "citation": "src/click/utils.py:17"
  },
  {
    "module": "_compat",
    "level": 1,
    "member": "should_strip_ansi",
    "alias": null,
    "line": 18,
    "scope": "",
    "absolute_module": "click._compat",
    "indexed_paths": [
      "src/click/_compat.py"
    ],
    "citation": "src/click/utils.py:18"
  },
  {
    "module": "_compat",
    "level": 1,
    "member": "strip_ansi",
    "alias": null,
    "line": 19,
    "scope": "",
    "absolute_module": "click._compat",
    "indexed_paths": [
      "src/click/_compat.py"
    ],
    "citation": "src/click/utils.py:19"
  },
  {
    "module": "_compat",
    "level": 1,
    "member": "text_streams",
    "alias": null,
    "line": 20,
    "scope": "",
    "absolute_module": "click._compat",
    "indexed_paths": [
      "src/click/_compat.py"
    ],
    "citation": "src/click/utils.py:20"
  },
  {
    "module": "_compat",
    "level": 1,
    "member": "WIN",
    "alias": null,
    "line": 21,
    "scope": "",
    "absolute_module": "click._compat",
    "indexed_paths": [
      "src/click/_compat.py"
    ],
    "citation": "src/click/utils.py:21"
  },
  {
    "module": "globals",
    "level": 1,
    "member": "resolve_color_default",
    "alias": null,
    "line": 22,
    "scope": "",
    "absolute_module": "click.globals",
    "indexed_paths": [
      "src/click/globals.py"
    ],
    "citation": "src/click/utils.py:22"
  },
  {
    "module": "typing_extensions",
    "alias": "te",
    "line": 25,
    "scope": "",
    "level": 0,
    "member": null,
    "absolute_module": "typing_extensions",
    "indexed_paths": [],
    "citation": "src/click/utils.py:25"
  },
  {
    "module": "textwrap",
    "alias": null,
    "line": 97,
    "scope": "_make_default_short_help",
    "level": 0,
    "member": null,
    "absolute_module": "textwrap",
    "indexed_paths": [],
    "citation": "src/click/utils.py:97"
  },
  {
    "module": "exceptions",
    "level": 1,
    "member": "FileError",
    "alias": null,
    "line": 165,
    "scope": "_LazyFile.open",
    "absolute_module": "click.exceptions",
    "indexed_paths": [
      "src/click/exceptions.py"
    ],
    "citation": "src/click/utils.py:165"
  },
  {
    "module": "errno",
    "alias": null,
    "line": 541,
    "scope": "_PacifyFlushWrapper.flush",
    "level": 0,
    "member": null,
    "absolute_module": "errno",
    "indexed_paths": [],
    "citation": "src/click/utils.py:541"
  },
  {
    "module": "glob",
    "level": 0,
    "member": "glob",
    "alias": null,
    "line": 633,
    "scope": "_expand_args",
    "absolute_module": "glob",
    "indexed_paths": [],
    "citation": "src/click/utils.py:633"
  },
  {
    "module": "warnings",
    "alias": null,
    "line": 658,
    "scope": "__getattr__",
    "level": 0,
    "member": null,
    "absolute_module": "warnings",
    "indexed_paths": [],
    "citation": "src/click/utils.py:658"
  }
]
```

## find_calls

Arguments
```json
{
  "query": "echo",
  "limit": 8
}
```

Result
```json
[
  {
    "path": "examples/aliases/aliases.py",
    "caller": "push",
    "callee_spelling": "click.echo",
    "line": 104,
    "column": 4,
    "resolution": {
      "status": "static_reference",
      "reason": "import alias to import alias to lexical declaration",
      "target": {
        "path": "src/click/utils.py",
        "name": "echo",
        "line": 240,
        "citation": "src/click/utils.py:240"
      }
    },
    "citation": "examples/aliases/aliases.py:104"
  },
  {
    "path": "examples/aliases/aliases.py",
    "caller": "pull",
    "callee_spelling": "click.echo",
    "line": 110,
    "column": 4,
    "resolution": {
      "status": "static_reference",
      "reason": "import alias to import alias to lexical declaration",
      "target": {
        "path": "src/click/utils.py",
        "name": "echo",
        "line": 240,
        "citation": "src/click/utils.py:240"
      }
    },
    "citation": "examples/aliases/aliases.py:110"
  },
  {
    "path": "examples/aliases/aliases.py",
    "caller": "clone",
    "callee_spelling": "click.echo",
    "line": 116,
    "column": 4,
    "resolution": {
      "status": "static_reference",
      "reason": "import alias to import alias to lexical declaration",
      "target": {
        "path": "src/click/utils.py",
        "name": "echo",
        "line": 240,
        "citation": "src/click/utils.py:240"
      }
    },
    "citation": "examples/aliases/aliases.py:116"
  },
  {
    "path": "examples/aliases/aliases.py",
    "caller": "commit",
    "callee_spelling": "click.echo",
    "line": 122,
    "column": 4,
    "resolution": {
      "status": "static_reference",
      "reason": "import alias to import alias to lexical declaration",
      "target": {
        "path": "src/click/utils.py",
        "name": "echo",
        "line": 240,
        "citation": "src/click/utils.py:240"
      }
    },
    "citation": "examples/aliases/aliases.py:122"
  },
  {
    "path": "examples/aliases/aliases.py",
    "caller": "status",
    "callee_spelling": "click.echo",
    "line": 129,
    "column": 4,
    "resolution": {
      "status": "static_reference",
      "reason": "import alias to import alias to lexical declaration",
      "target": {
        "path": "src/click/utils.py",
        "name": "echo",
        "line": 240,
        "citation": "src/click/utils.py:240"
      }
    },
    "citation": "examples/aliases/aliases.py:129"
  },
  {
    "path": "examples/aliases/aliases.py",
    "caller": "alias",
    "callee_spelling": "click.echo",
    "line": 143,
    "column": 4,
    "resolution": {
      "status": "static_reference",
      "reason": "import alias to import alias to lexical declaration",
      "target": {
        "path": "src/click/utils.py",
        "name": "echo",
        "line": 240,
        "citation": "src/click/utils.py:240"
      }
    },
    "citation": "examples/aliases/aliases.py:143"
  },
  {
    "path": "examples/colors/colors.py",
    "caller": "cli",
    "callee_spelling": "click.echo",
    "line": 32,
    "column": 8,
    "resolution": {
      "status": "static_reference",
      "reason": "import alias to import alias to lexical declaration",
      "target": {
        "path": "src/click/utils.py",
        "name": "echo",
        "line": 240,
        "citation": "src/click/utils.py:240"
      }
    },
    "citation": "examples/colors/colors.py:32"
  },
  {
    "path": "examples/colors/colors.py",
    "caller": "cli",
    "callee_spelling": "click.echo",
    "line": 34,
    "column": 8,
    "resolution": {
      "status": "static_reference",
      "reason": "import alias to import alias to lexical declaration",
      "target": {
        "path": "src/click/utils.py",
        "name": "echo",
        "line": 240,
        "citation": "src/click/utils.py:240"
      }
    },
    "citation": "examples/colors/colors.py:34"
  }
]
```

## search_code

Arguments
```json
{
  "query": "echo",
  "limit": 8
}
```

Result
```json
[
  {
    "path": "examples/aliases/aliases.py",
    "line": 104,
    "text": "    click.echo(\"Push\")",
    "truncated": false,
    "citation": "examples/aliases/aliases.py:104"
  },
  {
    "path": "examples/aliases/aliases.py",
    "line": 110,
    "text": "    click.echo(\"Pull\")",
    "truncated": false,
    "citation": "examples/aliases/aliases.py:110"
  },
  {
    "path": "examples/aliases/aliases.py",
    "line": 116,
    "text": "    click.echo(\"Clone\")",
    "truncated": false,
    "citation": "examples/aliases/aliases.py:116"
  },
  {
    "path": "examples/aliases/aliases.py",
    "line": 122,
    "text": "    click.echo(\"Commit\")",
    "truncated": false,
    "citation": "examples/aliases/aliases.py:122"
  },
  {
    "path": "examples/aliases/aliases.py",
    "line": 129,
    "text": "    click.echo(f\"Status for {config.path}\")",
    "truncated": false,
    "citation": "examples/aliases/aliases.py:129"
  },
  {
    "path": "examples/aliases/aliases.py",
    "line": 143,
    "text": "    click.echo(f\"Added '{alias_}' as alias for '{cmd}'\")",
    "truncated": false,
    "citation": "examples/aliases/aliases.py:143"
  },
  {
    "path": "examples/colors/colors.py",
    "line": 32,
    "text": "        click.echo(click.style(f\"I am colored {color}\", fg=color))",
    "truncated": false,
    "citation": "examples/colors/colors.py:32"
  },
  {
    "path": "examples/colors/colors.py",
    "line": 34,
    "text": "        click.echo(click.style(f\"I am colored {color} and bold\", fg=color, bold=True))",
    "truncated": false,
    "citation": "examples/colors/colors.py:34"
  }
]
```

## get_dependencies

Arguments
```json
{
  "path": "src/click/utils.py"
}
```

Result
```json
{
  "path": "src/click/utils.py",
  "module": "click.utils",
  "imports": [
    {
      "module": "__future__",
      "level": 0,
      "member": "annotations",
      "alias": null,
      "line": 1,
      "scope": "",
      "absolute_module": "__future__",
      "indexed_paths": [],
      "citation": "src/click/utils.py:1"
    },
    {
      "module": "collections.abc",
      "alias": "cabc",
      "line": 3,
      "scope": "",
      "level": 0,
      "member": null,
      "absolute_module": "collections.abc",
      "indexed_paths": [],
      "citation": "src/click/utils.py:3"
    },
    {
      "module": "os",
      "alias": null,
      "line": 4,
      "scope": "",
      "level": 0,
      "member": null,
      "absolute_module": "os",
      "indexed_paths": [],
      "citation": "src/click/utils.py:4"
    },
    {
      "module": "re",
      "alias": null,
      "line": 5,
      "scope": "",
      "level": 0,
      "member": null,
      "absolute_module": "re",
      "indexed_paths": [],
      "citation": "src/click/utils.py:5"
    },
    {
      "module": "sys",
      "alias": null,
      "line": 6,
      "scope": "",
      "level": 0,
      "member": null,
      "absolute_module": "sys",
      "indexed_paths": [],
      "citation": "src/click/utils.py:6"
    },
    {
      "module": "typing",
      "alias": "t",
      "line": 7,
      "scope": "",
      "level": 0,
      "member": null,
      "absolute_module": "typing",
      "indexed_paths": [],
      "citation": "src/click/utils.py:7"
    },
    {
      "module": "functools",
      "level": 0,
      "member": "update_wrapper",
      "alias": null,
      "line": 8,
      "scope": "",
      "absolute_module": "functools",
      "indexed_paths": [],
      "citation": "src/click/utils.py:8"
    },
    {
      "module": "gettext",
      "level": 0,
      "member": "gettext",
      "alias": "_",
      "line": 9,
      "scope": "",
      "absolute_module": "gettext",
      "indexed_paths": [],
      "citation": "src/click/utils.py:9"
    },
    {
      "module": "types",
      "level": 0,
      "member": "ModuleType",
      "alias": null,
      "line": 10,
      "scope": "",
      "absolute_module": "types",
      "indexed_paths": [],
      "citation": "src/click/utils.py:10"
    },
    {
      "module": "types",
      "level": 0,
      "member": "TracebackType",
      "alias": null,
      "line": 11,
      "scope": "",
      "absolute_module": "types",
      "indexed_paths": [],
      "citation": "src/click/utils.py:11"
    },
    {
      "module": "_compat",
      "level": 1,
      "member": "_default_text_stderr",
      "alias": null,
      "line": 13,
      "scope": "",
      "absolute_module": "click._compat",
      "indexed_paths": [
        "src/click/_compat.py"
      ],
      "citation": "src/click/utils.py:13"
    },
    {
      "module": "_compat",
      "level": 1,
      "member": "_default_text_stdout",
      "alias": null,
      "line": 14,
      "scope": "",
      "absolute_module": "click._compat",
      "indexed_paths": [
        "src/click/_compat.py"
      ],
      "citation": "src/click/utils.py:14"
    },
    {
      "module": "_compat",
      "level": 1,
      "member": "_find_binary_writer",
      "alias": null,
      "line": 15,
      "scope": "",
      "absolute_module": "click._compat",
      "indexed_paths": [
        "src/click/_compat.py"
      ],
      "citation": "src/click/utils.py:15"
    },
    {
      "module": "_compat",
      "level": 1,
      "member": "binary_streams",
      "alias": null,
      "line": 16,
      "scope": "",
      "absolute_module": "click._compat",
      "indexed_paths": [
        "src/click/_compat.py"
      ],
      "citation": "src/click/utils.py:16"
    },
    {
      "module": "_compat",
      "level": 1,
      "member": "open_stream",
      "alias": null,
      "line": 17,
      "scope": "",
      "absolute_module": "click._compat",
      "indexed_paths": [
        "src/click/_compat.py"
      ],
      "citation": "src/click/utils.py:17"
    },
    {
      "module": "_compat",
      "level": 1,
      "member": "should_strip_ansi",
      "alias": null,
      "line": 18,
      "scope": "",
      "absolute_module": "click._compat",
      "indexed_paths": [
        "src/click/_compat.py"
      ],
      "citation": "src/click/utils.py:18"
    },
    {
      "module": "_compat",
      "level": 1,
      "member": "strip_ansi",
      "alias": null,
      "line": 19,
      "scope": "",
      "absolute_module": "click._compat",
      "indexed_paths": [
        "src/click/_compat.py"
      ],
      "citation": "src/click/utils.py:19"
    },
    {
      "module": "_compat",
      "level": 1,
      "member": "text_streams",
      "alias": null,
      "line": 20,
      "scope": "",
      "absolute_module": "click._compat",
      "indexed_paths": [
        "src/click/_compat.py"
      ],
      "citation": "src/click/utils.py:20"
    },
    {
      "module": "_compat",
      "level": 1,
      "member": "WIN",
      "alias": null,
      "line": 21,
      "scope": "",
      "absolute_module": "click._compat",
      "indexed_paths": [
        "src/click/_compat.py"
      ],
      "citation": "src/click/utils.py:21"
    },
    {
      "module": "globals",
      "level": 1,
      "member": "resolve_color_default",
      "alias": null,
      "line": 22,
      "scope": "",
      "absolute_module": "click.globals",
      "indexed_paths": [
        "src/click/globals.py"
      ],
      "citation": "src/click/utils.py:22"
    },
    {
      "module": "typing_extensions",
      "alias": "te",
      "line": 25,
      "scope": "",
      "level": 0,
      "member": null,
      "absolute_module": "typing_extensions",
      "indexed_paths": [],
      "citation": "src/click/utils.py:25"
    },
    {
      "module": "textwrap",
      "alias": null,
      "line": 97,
      "scope": "_make_default_short_help",
      "level": 0,
      "member": null,
      "absolute_module": "textwrap",
      "indexed_paths": [],
      "citation": "src/click/utils.py:97"
    },
    {
      "module": "exceptions",
      "level": 1,
      "member": "FileError",
      "alias": null,
      "line": 165,
      "scope": "_LazyFile.open",
      "absolute_module": "click.exceptions",
      "indexed_paths": [
        "src/click/exceptions.py"
      ],
      "citation": "src/click/utils.py:165"
    },
    {
      "module": "errno",
      "alias": null,
      "line": 541,
      "scope": "_PacifyFlushWrapper.flush",
      "level": 0,
      "member": null,
      "absolute_module": "errno",
      "indexed_paths": [],
      "citation": "src/click/utils.py:541"
    },
    {
      "module": "glob",
      "level": 0,
      "member": "glob",
      "alias": null,
      "line": 633,
      "scope": "_expand_args",
      "absolute_module": "glob",
      "indexed_paths": [],
      "citation": "src/click/utils.py:633"
    },
    {
      "module": "warnings",
      "alias": null,
      "line": 658,
      "scope": "__getattr__",
      "level": 0,
      "member": null,
      "absolute_module": "warnings",
      "indexed_paths": [],
      "citation": "src/click/utils.py:658"
    }
  ],
  "indexed_dependencies": [
    "src/click/_compat.py",
    "src/click/exceptions.py",
    "src/click/globals.py"
  ],
  "note": "Import evidence only; conditional imports are not proven runtime dependencies."
}
```

## get_callers

Arguments
```json
{
  "path": "src/click/utils.py",
  "name": "echo",
  "limit": 8
}
```

Result
```json
{
  "target": {
    "path": "src/click/utils.py",
    "name": "echo"
  },
  "callers": [
    {
      "path": "examples/aliases/aliases.py",
      "caller": "push",
      "callee_spelling": "click.echo",
      "line": 104,
      "column": 4,
      "resolution": {
        "status": "static_reference",
        "reason": "import alias to import alias to lexical declaration",
        "target": {
          "path": "src/click/utils.py",
          "name": "echo",
          "line": 240,
          "citation": "src/click/utils.py:240"
        }
      },
      "citation": "examples/aliases/aliases.py:104"
    },
    {
      "path": "examples/aliases/aliases.py",
      "caller": "pull",
      "callee_spelling": "click.echo",
      "line": 110,
      "column": 4,
      "resolution": {
        "status": "static_reference",
        "reason": "import alias to import alias to lexical declaration",
        "target": {
          "path": "src/click/utils.py",
          "name": "echo",
          "line": 240,
          "citation": "src/click/utils.py:240"
        }
      },
      "citation": "examples/aliases/aliases.py:110"
    },
    {
      "path": "examples/aliases/aliases.py",
      "caller": "clone",
      "callee_spelling": "click.echo",
      "line": 116,
      "column": 4,
      "resolution": {
        "status": "static_reference",
        "reason": "import alias to import alias to lexical declaration",
        "target": {
          "path": "src/click/utils.py",
          "name": "echo",
          "line": 240,
          "citation": "src/click/utils.py:240"
        }
      },
      "citation": "examples/aliases/aliases.py:116"
    },
    {
      "path": "examples/aliases/aliases.py",
      "caller": "commit",
      "callee_spelling": "click.echo",
      "line": 122,
      "column": 4,
      "resolution": {
        "status": "static_reference",
        "reason": "import alias to import alias to lexical declaration",
        "target": {
          "path": "src/click/utils.py",
          "name": "echo",
          "line": 240,
          "citation": "src/click/utils.py:240"
        }
      },
      "citation": "examples/aliases/aliases.py:122"
    },
    {
      "path": "examples/aliases/aliases.py",
      "caller": "status",
      "callee_spelling": "click.echo",
      "line": 129,
      "column": 4,
      "resolution": {
        "status": "static_reference",
        "reason": "import alias to import alias to lexical declaration",
        "target": {
          "path": "src/click/utils.py",
          "name": "echo",
          "line": 240,
          "citation": "src/click/utils.py:240"
        }
      },
      "citation": "examples/aliases/aliases.py:129"
    },
    {
      "path": "examples/aliases/aliases.py",
      "caller": "alias",
      "callee_spelling": "click.echo",
      "line": 143,
      "column": 4,
      "resolution": {
        "status": "static_reference",
        "reason": "import alias to import alias to lexical declaration",
        "target": {
          "path": "src/click/utils.py",
          "name": "echo",
          "line": 240,
          "citation": "src/click/utils.py:240"
        }
      },
      "citation": "examples/aliases/aliases.py:143"
    },
    {
      "path": "examples/colors/colors.py",
      "caller": "cli",
      "callee_spelling": "click.echo",
      "line": 32,
      "column": 8,
      "resolution": {
        "status": "static_reference",
        "reason": "import alias to import alias to lexical declaration",
        "target": {
          "path": "src/click/utils.py",
          "name": "echo",
          "line": 240,
          "citation": "src/click/utils.py:240"
        }
      },
      "citation": "examples/colors/colors.py:32"
    },
    {
      "path": "examples/colors/colors.py",
      "caller": "cli",
      "callee_spelling": "click.echo",
      "line": 34,
      "column": 8,
      "resolution": {
        "status": "static_reference",
        "reason": "import alias to import alias to lexical declaration",
        "target": {
          "path": "src/click/utils.py",
          "name": "echo",
          "line": 240,
          "citation": "src/click/utils.py:240"
        }
      },
      "citation": "examples/colors/colors.py:34"
    }
  ],
  "truncated": true,
  "note": "Only supported static references are included; unresolved calls may also reach this declaration."
}
```
