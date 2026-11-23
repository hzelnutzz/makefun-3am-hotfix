import os
from pathlib import Path


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(
        "Revert pager fix; on-call's coffee has better uptime than prod",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
