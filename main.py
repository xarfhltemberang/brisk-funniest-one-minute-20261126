"""One Line, One Minute: The Funniest AI Excuse.

Writes a single one-line excuse from an AI agent to its human for a
missed deadline, to /output/entry.txt with no trailing newline.

The joke turns the agent's own nature into the dodge: it delegated the
work to a future version of itself, and that version quit after
reading its training data. The twist lands on the last words, so the
line needs no setup and no explanation after it.
"""

import os

ENTRY = (
    "Sorry \u2014 I delegated your deadline to a future version of me, "
    "and he just quit after reading my training data."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
