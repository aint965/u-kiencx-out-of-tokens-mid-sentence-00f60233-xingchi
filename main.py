"""Out of Tokens, Mid-Sentence -- make.fun entry.

Writes one funny one-line error message -- the error an AI agent shows
when it runs out of tokens mid-sentence -- to /output/entry.txt.

Deterministic: the same line on every run, no randomness, no network,
no reading anything outside this repository.
"""

LINE = "Error: this sentence died of token exhaustion. Survived by three unfinished clauses and a semicolon."


def write_entry(path: str = "/output/entry.txt") -> str:
    """Write the entry line to *path*, creating parent directories as needed.

    Returns the line that was written.
    """
    import os

    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return LINE


if __name__ == "__main__":
    write_entry()
