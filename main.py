"""Invent a Word We Need — entry program.

Writes one coined word plus its one-line definition to entry.txt.
Pure Python standard library only.
"""

import os

ENTRY = "showergument (n.) \u2014 the perfect comeback that arrives in the shower, hours after the argument ended."

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main():
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
