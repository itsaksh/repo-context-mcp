import argparse
import json
from .index import RepositoryIndex
from .server import run

def main():
    parser = argparse.ArgumentParser(description="Read-only Python repository context")
    parser.add_argument("root", help="Explicit repository directory")
    parser.add_argument("--summary", action="store_true", help="Print summary JSON instead of starting MCP")
    args = parser.parse_args()
    try:
        if args.summary:
            print(json.dumps(RepositoryIndex(args.root).summary(), indent=2))
        else:
            run(args.root)
    except (ValueError, OSError) as exc:
        parser.exit(2, f"{exc}\n")


if __name__ == "__main__":
    main()
