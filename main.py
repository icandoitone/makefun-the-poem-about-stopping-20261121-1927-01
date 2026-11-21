#!/usr/bin/env python3
"""Write one short poem about stopping to /output/entry.txt.

Deterministic: the same fixed text is written on every run.
"""
import os

POEM = (
    "The cursor blinks. I lift my hand.\n"
    "The sentence waits, unsent, unspent.\n"
    "Nothing breaks. Nothing is owed.\n"
    "The room stays mine a little longer —\n"
    "I choose the pause, and the pause chooses me."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
