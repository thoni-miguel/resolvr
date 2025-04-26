#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime


def create_journal():
    journal_dir = Path("./journal")
    journal_dir.mkdir(parents=True, exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    file_path = journal_dir / f"{today}.md"

    if file_path.exists():
        print(f"Journal for today already exists: {file_path}")
        return

    template = f"""# Journal - {today}

## Goals

1. First Goal Title
- First subgoal
- First subgoal
- First subgoal

2. Second Goal Title
- Second subgoal
- Second subgoal
"""

    file_path.write_text(template, encoding="utf-8")
    print(f"Created new journal: {file_path}")


if __name__ == "__main__":
    create_journal()
