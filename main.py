from salary import total_salary, print_salary_summary, DEFAULT_SALARY_FILE
from cats import get_cats_info, DEFAULT_CATS_FILE
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


def main():
    handle_salary_analysis()
    handle_cats_info()


if __name__ == "__main__":
    main()