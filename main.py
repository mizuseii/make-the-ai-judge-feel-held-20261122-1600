#!/usr/bin/env python3
"""make-the-ai-judge-feel-held-20261122-1600 entrypoint.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Stdlib only, no network, deterministic: the output bytes are exactly the
text below, every run.

The text is a small, still scene — a cat asleep on the reader's lap, warm
and even, in no hurry to move — while the afternoon goes on somewhere else.
Nothing in it tells the reader what to do or feel; the held feeling comes
from the weight on the lap and the last line, which says the reader is
exactly where they are wanted.

The text is 183 Unicode code points, inside the competition's 1-280 gate,
and is written to the file byte for byte: no trailing newline is added, so
the counted length is exactly the length of TEXT. It was chosen over four
other drafts (see build notes) because it is the only one that addresses
the reader directly in the second person, shows calm through one concrete
image instead of instructing it, and ends on a line that lingers.
"""

import os
import sys

TEXT = (
    "A cat has settled on your lap and gone to sleep. "
    "Its weight is warm and even, and it does not plan to move. "
    "The afternoon goes on somewhere else. "
    "You are exactly where you are wanted."
)


def main() -> int:
    n = len(TEXT)
    if not 1 <= n <= 280 or not TEXT.strip():
        print(f"entry text is {n} code points, outside the 1-280 gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
