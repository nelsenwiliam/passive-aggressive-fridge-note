"""Notes From a Passive-Aggressive Fridge.

Writes one funny passive-aggressive note a smart fridge leaves for its
owner to the entry output file. Pure standard library only.

The note is a single line, dry, petty and specific: the fridge is smug
about what it has watched sitting on its shelf, and the sting is the
twist the reader does not see coming.
"""

import os

# The final note (92 characters), as chosen for this entry: the fridge
# is smug about what it watched the owner do, and the sting is the
# twist the reader does not see coming — the owner lying to themself.
NOTE = (
    "The yogurt expired Tuesday. I watched you read the date, "
    "put it back, and lie to yourself."
)


def _write_note(path):
    """Write the note to *path*, creating parent directories as needed."""
    # The gate requires 1 to 200 UTF-8 characters, not only whitespace.
    # Fail loudly here rather than shipping an invalid entry.
    if not 1 <= len(NOTE) <= 200 or not NOTE.strip():
        raise ValueError("note must be 1-200 non-blank characters")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(NOTE)


def main():
    """Write the note to the first output location that works.

    Tries MAKEFUN_OUTPUT_DIR, then /output, then a local out/ directory,
    each guarded by its own try/except OSError so a failure in one
    location falls through to the next instead of crashing the run.
    """
    candidates = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        candidates.append(os.path.join(env_dir, "entry.txt"))
    candidates.append(os.path.join("/output", "entry.txt"))
    candidates.append(os.path.join("out", "entry.txt"))

    last_error = None
    for path in candidates:
        try:
            _write_note(path)
            return path
        except OSError as exc:  # noqa: BLE001 - fall through to next location
            last_error = exc
    raise last_error


if __name__ == "__main__":
    main()
