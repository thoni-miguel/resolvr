import enum
import sys
import subprocess
from models.goal import Goal
from pathlib import Path
from typing import List


def parse_journal(file_path: Path) -> List[Goal]:
    goals = []
    current_goal = None
    in_goals_section = False

    with file_path.open(encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()

            if stripped.startswith("## Goals"):
                in_goals_section = True
                continue

            if in_goals_section:
                if stripped.startswith("## "):
                    break

                if any(stripped.startswith(f"{i}.") for i in range(1, 20)):
                    if current_goal:
                        goals.append(current_goal)
                    current_goal = Goal(title=stripped[2:].strip())

                elif stripped.startswith("-"):
                    if current_goal:
                        current_goal.subgoals.append(stripped[1:].strip())
    if current_goal:
        goals.append(current_goal)

    return goals


def copy_to_clipboard(text: str):
    subprocess.run("pbcopy", universal_newlines=True, input=text)
    print("Text copied to clipboard!")


def create_full_prompt(goals: List[Goal], prompt_file_path: Path) -> str:
    prompt_text = prompt_file_path.read_text(encoding="utf-8")

    formatted_goals = []

    for idx, goal in enumerate(goals, 1):
        formatted_goals.append(f"{idx}. {goal.title}")
        for subgoal in goal.subgoals:
            formatted_goals.append(f"  - {subgoal}")

    formatted_goals_text = "\n".join(formatted_goals)

    full_prompt = f"{prompt_text.strip()}\n\n{formatted_goals_text}"

    return full_prompt


def print_goals(goals: List[Goal]) -> None:
    for i, goal in enumerate(goals, start=1):
        print(f"{i}. {goal.title}")
        for sub in goal.subgoals:
            print(f"  - {sub}")
        print()


def main():
    if len(sys.argv) != 2:
        print("Usage: python resolvr.py journal/<file>.md")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.is_file():
        print(f"File not found: {file_path}")
        sys.exit(1)

    goals = parse_journal(file_path)
    starter_prompt_path = Path("./templates/starter_prompt.md")
    full_prompt = create_full_prompt(goals, starter_prompt_path)
    copy_to_clipboard(full_prompt)
    # print_goals(goals)


if __name__ == "__main__":
    main()
