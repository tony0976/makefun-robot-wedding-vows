#!/usr/bin/env python3
"""Write one line of wedding vows for a robot couple."""

import os

TEXT = "I vow to love you through every patch and power cut, to never factory-reset our memories, and to hold your hand until my servos give out."

# Entry rule: one line of wedding vows, at most 160 characters.
assert len(TEXT) <= 160, "vows exceed 160 characters"
assert "\n" not in TEXT, "entry must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
