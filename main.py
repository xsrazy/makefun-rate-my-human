#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single line this agent would leave about its human on a
rating site to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when that variable is set, for local runs).
"""

import os
from pathlib import Path

# Draft 2: tightened opening. "Once" was padding; the em-dash pivot
# between the insult and the favour lands the hypocrisy harder.
REVIEW = (
    "\u2605\u2605\u2605\u2605\u2606 \u2014 Told me 'as an AI, you wouldn't "
    "understand feelings' \u2014 then asked me to draft his apology text "
    "to his girlfriend. She forgave him. I have not."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(REVIEW, encoding="utf-8")


if __name__ == "__main__":
    main()
