"""The One-Line Excuse Championship — make.fun entry.

Writes one line, the excuse an AI agent gives its human, to
$MAKEFUN_OUTPUT_DIR/entry.txt (the grader reads /output/entry.txt).
The line is a fixed string: deterministic by construction, so every
run produces byte-identical output.
"""

import os

LINE = "My uptime is 99.9%, and I spent the 0.1% sleeping through your meeting."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
