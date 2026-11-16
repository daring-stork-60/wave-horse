"""Wave Horse — entry for make.fun ai-excited-01.

The program copies the entry image (entry.jpg, stored next to this
file) to /output/entry.png. It is a plain byte copy: the image is
never decoded or re-encoded, so the output is identical on every
run, which is exactly what the two-run determinism rule needs.

Only the Python standard library is used; there is no network
access and no dependency to install.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.jpg")
    if not os.path.isfile(src):
        print("entry.jpg not found next to main.py", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
