from .analyzer import total_salary, print_salary_summary, DEFAULT_SALARY_FILE


def main():
    result = total_salary(DEFAULT_SALARY_FILE)
    if result is not None:
        print_salary_summary(*result)


if __name__ == "__main__":
    main()
