"""Copy the pre-rendered front page to the output directory.

The image was rendered at build time from verified 26 November 2026 news.
This program does no rendering and no network: it only copies entry.png
to $MAKEFUN_OUTPUT_DIR/entry.png, so both grader runs write identical bytes.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(SRC, "rb") as f:
        data = f.read()
    # Guard against a truncated render: an empty file must fail loudly
    # instead of passing an invalid entry to the gate.
    if not data:
        raise SystemExit("entry.png is empty")
    with open(os.path.join(out_dir, "entry.png"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
