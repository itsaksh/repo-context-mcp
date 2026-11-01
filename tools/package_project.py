"""Create a reviewable project archive without caches or local credentials."""
from pathlib import Path
import zipfile

root = Path(__file__).resolve().parents[1]
output = root.parents[1]/"Repository_Context_MCP_Project1.zip"
with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if not path.is_file() or path.is_symlink() or any(p in {".git", ".venv", "__pycache__", "build", "_qa"} or p.endswith(".egg-info") for p in relative.parts):
            continue
        archive.write(path, f"repo-context-mcp/{relative.as_posix()}")
with zipfile.ZipFile(output) as archive:
    assert archive.testzip() is None
    required = {"repo-context-mcp/evidence/click-demo.html", "repo-context-mcp/evidence/CLICK_LICENSE.txt",
                "repo-context-mcp/evidence/test-results.json", "repo-context-mcp/tests/test_sdk.py"}
    assert required <= set(archive.namelist())
    print(f"{output}\n{len(archive.namelist())} files\n{output.stat().st_size} bytes")
