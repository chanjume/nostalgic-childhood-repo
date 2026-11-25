#!/usr/bin/env python3
"""Write one childhood-memory sentence to /output/entry.txt.

The line: the streetlights switching on at 6 p.m. as the only curfew
a neighbourhood of kids ever obeyed, because the game of tag was not
over until the last kid was caught. It is grounded in a concrete
sensation (the buzzing streetlights, 6 p.m.), a real small detail
(nobody wanted to be the one who went home first), and it leaves the
warm ache of a summer evening that is gone but still lit.
"""
import os

ENTRY = "The streetlights buzzed on at 6 p.m. and that was the only curfew we ever obeyed — because the game of tag wasn't over until the last kid was caught, and nobody wanted to be the one who went home first."


def main():
    assert 1 <= len(ENTRY) <= 280, f"entry must be 1-280 characters, got {len(ENTRY)}"
    # One sentence, one line: no leading/trailing whitespace, no newline inside.
    # The trailing newline in the file is the file's line ending, not part of the sentence.
    assert ENTRY.strip() == ENTRY, "no leading/trailing whitespace"
    assert "\n" not in ENTRY, "must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
