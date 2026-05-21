from pathlib import Path

from console_ui import print_error, print_success
from file_reader import read_text_lines

EXPECTED_FORMAT = "Ім'я Прізвище,зарплата (наприклад, 'Alex Korp,3000' або 'Alex Korp,3000.50')"
DEFAULT_SALARY_FILE = Path(__file__).parent / "salary.txt"


def total_salary(path):
    lines = read_text_lines(path)
    if lines is None:
        return None

    salaries = []
    for line_num, line in enumerate(lines, start=1):
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        if len(parts) != 2:
            print_error(
                f"Помилка обробки файлу '{path}' (рядок {line_num}): некоректний формат даних.\n"
                f"  Отримано:    '{line}' (знайдено {len(parts)} полів, очікується 2)\n"
                f"  Очікується:  {EXPECTED_FORMAT}"
            )
            return None

        _, salary_str = parts
        try:
            salaries.append(float(salary_str))
        except ValueError:
            print_error(
                f"Помилка обробки файлу '{path}' (рядок {line_num}): некоректне значення зарплати.\n"
                f"  Отримано:    '{salary_str}' (не є числом)\n"
                f"  Очікується:  числове значення (наприклад, 3000 або 3000.50)"
            )
            return None

    total = sum(salaries)
    average = total / len(salaries) if salaries else 0
    return total, average


def print_salary_summary(total, average):
    total_label = "Загальна сума заробітної плати:"
    average_label = "Середня заробітна плата:"
    label_width = max(len(total_label), len(average_label))
    print_success(
        f"{total_label:<{label_width}}  {total}\n"
        f"{average_label:<{label_width}}  {average}"
    )
