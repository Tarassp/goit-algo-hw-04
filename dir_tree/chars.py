from enum import StrEnum


class TreeChar(StrEnum):
    BRANCH = "├── "
    LAST = "└── "
    PIPE = "│   "
    SPACE = "    "
