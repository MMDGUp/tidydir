import argparse
import sys
from .core import organize_directory

def main():
    parser = argparse.ArgumentParser(
        description="Organize files in a directory by type."
    )
    parser.add_argument("path", help="Path to the directory to organize")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed output"
    )

    args = parser.parse_args()

    try:
        organize_directory(args.path, dry_run=args.dry_run, verbose=args.verbose)
        print("✅ Done!")
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()