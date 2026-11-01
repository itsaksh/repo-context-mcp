"""Print a portable MCP host configuration without changing any host settings."""
import argparse
import json
from pathlib import Path
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("repository", type=Path)
args = parser.parse_args()
repository = args.repository.resolve(strict=True)
if not repository.is_dir():
    parser.error("repository must be a directory")
print(json.dumps({"mcpServers": {"repo-context": {
    "command": sys.executable,
    "args": [str(Path(__file__).resolve().parents[1]/"server_entry.py"), str(repository)],
}}}, indent=2))
