#!/usr/bin/env python3
"""Entry for make.fun bounty "The Word You'd Delete From the Dictionary".

The pick: floccinaucinihilipilification (29 letters) -- the longest
non-technical word in English, meaning "the act of estimating something
as worthless". Deleting it is the dictionary's own verdict on it: the
word for "worthless" is itself declared worthless and erased. The joke
lands at first sight from the word's absurd sound and length, comes
straight from the word itself, and leaves a real gap -- no other single
word means "estimating something as worthless".

This program writes exactly that one word, and nothing else, to
/output/entry.txt (UTF-8, no trailing newline, so the file holds one
word only). Standard library only, fully deterministic.
"""

import os

WORD = "floccinaucinihilipilification"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    # Self-check against the bounty gate: 1-77 UTF-8 chars, not only
    # whitespace, exactly one word. Fail loudly instead of shipping
    # an entry the gate would refuse.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert 1 <= len(written) <= 77, "entry must be 1-77 characters"
    assert written.strip(), "entry must not be only whitespace"
    assert written.split() == [written], "entry must be exactly one word"
    assert written == WORD, "entry must be the chosen word"


if __name__ == "__main__":
    main()
