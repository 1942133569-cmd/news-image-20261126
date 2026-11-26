# A make.fun news-image entry (Python 3.13, standard library only).
#
# The entry is the image beside this file: a newspaper front page that sums
# up the world news of Thursday 26 November 2026. This program copies it
# to /output/entry.png, deterministically, with no network access.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DEST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DEST = os.path.join(DEST_DIR, "entry.png")


def main():
    os.makedirs(DEST_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    # Sanity check: the output must be a whole PNG, so confirm its magic bytes.
    with open(DEST, "rb") as handle:
        if handle.read(8) != b"\x89PNG\r\n\x1a\n":
            raise SystemExit("entry.png is not a PNG")
    return 0


if __name__ == "__main__":
    sys.exit(main())
