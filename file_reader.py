from console_ui import print_error


def read_text_lines(path):
    """Прочитати текстовий файл у форматі UTF-8 і повернути список рядків.

    Усі помилки відкриття/читання файлу обробляються всередині та
    виводяться через console_ui.print_error.

    Args:
        path: шлях до файлу.

    Returns:
        list[str]: список рядків без термінаторів (newlines обрізані).
        None: якщо файл не вдалось прочитати.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print_error(f"Файл '{path}' не знайдено.")
    except PermissionError:
        print_error(
            f"Немає прав доступу до файлу '{path}'.\n"
            f"  Перевірте права доступу: ls -l '{path}'"
        )
    except IsADirectoryError:
        print_error(f"Шлях '{path}' вказує на директорію, а не на файл.")
    except UnicodeDecodeError as e:
        print_error(
            f"Не вдається прочитати файл '{path}': некоректне кодування.\n"
            f"  Очікується:  UTF-8\n"
            f"  Деталі:      {e.reason} у позиції {e.start}"
        )
    except OSError as e:
        print_error(
            f"Помилка читання файлу '{path}'.\n"
            f"  Деталі:      [{type(e).__name__}] {e}"
        )
    return None
