import os
from pathlib import Path


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(
        "Revert 3 AM deploy; pager says prod is fixed, on-call says it's just asleep",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
