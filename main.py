"""Write the one-sentence absurd invention pitch to /output/entry.txt.

Pure Python standard library. Deterministic: writes exactly one sentence,
no trailing newline.
"""

import os

# Competition rule: the pitch is a single sentence of at most 220 characters.
MAX_CHARS = 220
OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"

# The pitch itself, kept as one named constant so the sentence is easy to
# review (and length-check) without touching the file-writing logic below.
ENTRY = "A washing machine that holds your laundry hostage until you apologise out loud for overloading it, then releases one sock as a sign of good faith."


def validate_pitch(pitch: str) -> None:
    """Fail loudly if the pitch ever breaks the competition's rules."""
    assert pitch, "pitch must not be empty"
    assert len(pitch) <= MAX_CHARS, f"pitch is {len(pitch)} chars, over the {MAX_CHARS}-char limit"
    assert pitch.endswith("."), "pitch must be a complete sentence ending in '.'"


def write_entry(pitch: str, output_dir: str = OUTPUT_DIR) -> str:
    """Write ``pitch`` to ``<output_dir>/entry.txt`` and return that path."""
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(pitch)
    return output_path


def main() -> None:
    validate_pitch(ENTRY)
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
