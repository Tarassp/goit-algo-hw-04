from console_ui import print_warning
from file_reader import read_text_lines
from pathlib import Path

CAT_FIELDS = ("id", "name", "age")
DEFAULT_CATS_FILE = Path(__file__).parent / "cats_file.txt"

def get_cats_info(path):
    lines = read_text_lines(path)
    if lines is None:
        return []

    cats = []
    for line_num, line in enumerate(lines, start=1):
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        if len(parts) != len(CAT_FIELDS):
            print_warning(
                f"Попередження: рядок {line_num} у файлі '{path}' має некоректний формат.\n"
                f"  Отримано:    '{line}' (знайдено {len(parts)} полів, очікується {len(CAT_FIELDS)})\n"
                f"  Очікується:  {','.join(CAT_FIELDS)} (наприклад, '60b90c1c,Tom,3')\n"
                f"  Рядок пропущено."
            )
            continue
        cats.append(dict(zip(CAT_FIELDS, parts)))

    return cats