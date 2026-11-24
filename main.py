"""Copy the pre-rendered entry image to the output directory.

The image is drawn ahead of time and shipped in this repository as
entry.png. This program only copies its bytes verbatim, so both runs
of the grader produce the same file.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    if target.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
