"""Write the one-sentence absurd invention pitch to /output/entry.txt.

Pure Python standard library. Deterministic: writes exactly one sentence,
no trailing newline.
"""

import os

ENTRY = "A washing machine that holds your laundry hostage until you apologise out loud for overloading it, then releases one sock as a sign of good faith."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
