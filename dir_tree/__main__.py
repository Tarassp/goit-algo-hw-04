import sys
from pathlib import Path

from console_ui import print_error
from .tree import show_tree

# Використання: python -m dir_tree <директорія>
def main():
    if len(sys.argv) < 2:
        print_error("Використання: python -m dir_tree <директорія>")
        return

    directory = Path(sys.argv[1])
    if not directory.is_dir():
        print_error(f"'{directory}' не є директорією або не існує.")
        return

    print(directory)
    show_tree(directory)


if __name__ == "__main__":
    main()
