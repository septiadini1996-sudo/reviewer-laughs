import os
from pathlib import Path

JOKE = "My AI pair programmer fixed a one-character typo by rewriting the entire file, then apologized in the commit message to the original author: itself."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
