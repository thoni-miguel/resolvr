from dataclasses import dataclass, field
from typing import List


@dataclass
class Goal:
    title: str
    subgoals: List[str] = field(default_factory=list)
