"""Sorry, I Heard That Wrong — make.fun bounty entry.

Writes one line — the apology a smart speaker gives its owner after
mishearing them — to /output/entry.txt.

Rules (sealed gate): the file must be UTF-8 text of 1 to 140 characters,
not only whitespace, a single line. The program validates the line
before writing it, so a bad line fails loudly here instead of at the
gate. Deterministic: the same line every run, no randomness, no network,
stdlib only.
"""

import os
import sys

# v3: same morgue mishear, but the ending is pure device voice — the
# speaker offers its standard follow-up ("Shall I leave a message?")
# as if it had just called any ordinary contact. Shorter, tighter,
# and the twist lands on the very last words.
LINE = (
    "Sorry, I heard 'call Mom' as 'call the morgue.' "
    "She's on hold. Shall I leave a message?"
)

MAX_CHARS = 140


def main() -> int:
    line = LINE
    if not line or not line.strip():
        print("error: line is empty or whitespace only", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"error: line is {len(line)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    try:
        line.encode("ascii")
    except UnicodeEncodeError:
        print("error: line is not ASCII", file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the line, nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
