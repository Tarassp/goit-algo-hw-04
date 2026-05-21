"""
Для перевірки всіх завдань одразу запустіть цей файл:
    python main.py

Або запустіть кожен пакет окремо за патерном:
    python -m <package_name>

Доступні пакети: salary, cats, dir_tree (приймає шлях до директорії аргументом).
"""

from pathlib import Path

from salary import total_salary, print_salary_summary, DEFAULT_SALARY_FILE
from cats import get_cats_info, DEFAULT_CATS_FILE
from dir_tree import show_tree
from console_ui import print_title, print_success_items


def handle_salary_analysis():
    print_title("Task 1: Аналіз заробітних плат")
    result = total_salary(DEFAULT_SALARY_FILE)
    if result is not None:
        print_salary_summary(*result)


def handle_cats_info():
    print_title("Task 2: Інформація про котів")
    cats = get_cats_info(DEFAULT_CATS_FILE)
    print_success_items(cats)

def handle_directory_tree():
    path = Path(".")
    print_title("Task 3: Дерево директорії")
    print(path.absolute())
    show_tree(path)

def main():
    handle_salary_analysis()
    handle_cats_info()
    handle_directory_tree()


if __name__ == "__main__":
    main()