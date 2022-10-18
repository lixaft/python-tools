"""Reindent json files."""
from __future__ import annotations

import argparse
import json
import sys
from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point of the command line interface."""
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="+")
    parser.add_argument("-i", "--indent", type=int, default=2)

    args = parser.parse_args(argv)

    for filename in args.filenames:
        with open(filename, "r", encoding="utf-8") as stream:
            contents = json.load(stream)

        with open(filename, "w", encoding="utf-8") as stream:
            json.dump(contents, stream, indent=args.indent)

    return 0


if __name__ == "__main__":
    sys.exit(main())