#!/usr/bin/env python3
"""One Line, Big Laugh — entry program.

Writes a single original funny line to /output/entry.txt.
Stdlib only, no network, no input files.
"""

import os

LINE = (
    "My horoscope said 'avoid financial decisions today,' so I bought "
    "a telescope to watch my savings disappear in high definition."
)
# The joke: the setup promises obedience to the horoscope, then the
# punchline disobeys it in the most literal, over-equipped way possible —
# a telescope bought to watch the savings vanish in high definition.


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
