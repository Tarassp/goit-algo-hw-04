from console_ui.colors import YELLOW, BLUE, RED, BOLD, RESET

from .chars import TreeChar
from .icons import get_file_icon

IGNORED = {".git", "__pycache__", ".venv", "venv", "node_modules", ".DS_Store"}


def show_tree(directory, prefix=""):
    try:
        entries = [p for p in sorted(directory.iterdir()) if p.name not in IGNORED]
    except PermissionError:
        print(f"{prefix}{TreeChar.LAST}{RED}{BOLD}⛔ Немає доступу{RESET}")
        return

    for i, path in enumerate(entries):
        is_last = i == len(entries) - 1
        connector = TreeChar.LAST if is_last else TreeChar.BRANCH

        if path.is_file():
            icon = get_file_icon(path)
            print(f"{prefix}{connector}{YELLOW}{BOLD}{icon} {path.name}{RESET}")
        elif path.is_dir():
            print(f"{prefix}{connector}{BLUE}{BOLD}📁 {path.name}/{RESET}")
            extension = TreeChar.SPACE if is_last else TreeChar.PIPE
            show_tree(path, prefix + extension)
