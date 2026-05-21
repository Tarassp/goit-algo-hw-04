# goit-algo-hw-04

Чотири незалежні задачі, об'єднані в один проєкт. Спільна інфраструктура (кольоровий консольний вивід, читання файлів) винесена в окремі пакети й перевикористовується між задачами.

## Запуск

Перевірити всі задачі послідовно:

```bash
python main.py
```

Або запустити кожен пакет окремо:

```bash
python -m salary
python -m cats
python -m dir_tree <шлях_до_директорії>
python -m personal_assistant
```

---

## Задача 1 — Аналіз заробітних плат (`salary`)

Зчитує текстовий файл із зарплатами у форматі `Ім'я Прізвище,зарплата` (наприклад, `Alex Korp,3000`) і виводить **загальну суму** та **середнє значення** зарплати.

- Файл за замовчуванням: [salary/salary.txt](salary/salary.txt)
- Рядки з некоректним форматом або нечисловою зарплатою спиняють обробку з діагностичним повідомленням, що вказує номер проблемного рядка та що очікувалось.

## Задача 2 — Інформація про котів (`cats`)

Зчитує файл із даними про котів у форматі `id,name,age` (наприклад, `60b90c1c...,Tom,3`) і повертає список словників. Рядки з некоректною кількістю полів пропускаються з попередженням, але обробка триває.

- Файл за замовчуванням: [cats/cats_file.txt](cats/cats_file.txt)

## Задача 3 — Дерево директорій (`dir_tree`)

Рекурсивно друкує структуру директорії з кольоровим підсвічуванням, іконками за розширенням файлу та обходом «службових» папок (`.git`, `__pycache__`, `.venv`, `venv`, `node_modules`, `.DS_Store`).

- Підтримує понад 30 розширень + спеціальні імена (`README.md`, `Dockerfile`, `LICENSE`, `Makefile`, …).
- `python -m dir_tree <path>` — приймає шлях аргументом, валідує існування директорії.
- При запуску з `main.py` показує поточну директорію (`Path(".")`).

---

## Задача 4 — Персональний помічник (`personal_assistant`)

Інтерактивний консольний бот для зберігання контактів. Працює як REPL — приймає команди з клавіатури до моменту виходу. Дані живуть лише в пам'яті поточної сесії.

### Команди

| Команда | Аргументи | Опис |
|---|---|---|
| `hello` | — | Привітання |
| `add` | `<name> <phone>` | Додати контакт |
| `change` | `<name> <phone>` | Змінити номер існуючого контакту |
| `phone` | `<name>` | Показати номер контакту |
| `all` | — | Показати всі контакти у вигляді таблиці |
| `close` / `exit` | — | Завершити роботу |

### Валідація

- **Телефон** має містити лише цифри (`1234`, `0975551234`). Дефіси, пробіли, літери — відхиляються.
- **Невідома команда** або порожній ввід → `Invalid command.`
- **Відсутній контакт** у `phone`/`change` → `Contact not found.` (для `change` перевірка існування передує перевірці формату телефона).
- **Неправильна кількість аргументів** → конкретна підказка (`Give me name and phone please.`, `Give me name please.`, …).

### Кольоровий вивід

Презентаційний шар розрізняє три рівні повідомлень через `enum Severity`:

| Колір | Severity | Кейси |
|---|---|---|
| 🟢 Зелений | `SUCCESS` | успішні операції, `hello`, результат `phone`/`all`, `Good bye!` |
| 🟡 Жовтий | `WARNING` | уточнення (брак аргументів, поганий формат телефона), `Contact not found.` |
| 🔴 Червоний | `ERROR` | невідома або порожня команда (`Invalid command.`) |

### Архітектура

Пакет розбито за принципом single-responsibility — бізнес-логіка відокремлена від презентації:

- [`commands.py`](personal_assistant/commands.py) — `Command(StrEnum)` з переліком валідних команд.
- [`exceptions.py`](personal_assistant/exceptions.py) — типізовані винятки: `EmptyInputError`, `UnknownCommandError`, `InvalidArgsError`, `ContactNotFoundError`, `ExitSignal`.
- [`parse_input.py`](personal_assistant/parse_input.py) — `parse_input(raw) -> (Command, args)`. Невалідний ввід кидає винятки, не повертає `None`.
- [`handlers.py`](personal_assistant/handlers.py) — фабрика `make_handlers()`, що повертає `dict[Command, HandlerType]`. Обробники тримають `contacts` через **замикання** — інкапсульований стан без глобальних змінних. Помилки сигналізуються **винятками**, а не магічними рядками.
- [`bot.py`](personal_assistant/bot.py) — диспатчер `process_command` (чиста функція, без I/O) і REPL `run`. Мапить виняток → `Severity` → принтер із `console_ui`.
- [`formatters.py`](personal_assistant/formatters.py) — побудова таблиці контактів із box-drawing символами та вирівнюванням колонок під найдовші значення.
- [`__main__.py`](personal_assistant/__main__.py) — тонкий entry point: `from .bot import run`.

Команди `exit`/`close` обидві мапляться на один обробник `handle_exit`, який кидає `ExitSignal` — диспатчер ловить його як спецсигнал на завершення REPL.

### Тестування без I/O

`process_command` — чиста функція, тестується без `input()`:

```python
from personal_assistant import make_handlers, process_command

h = make_handlers()
assert process_command("add John 1234", h)[0] == "Contact added."
assert process_command("phone John", h)[0] == "1234"
assert process_command("foo", h)[0] == "Invalid command."
```

### Приклад сесії

```
Welcome to the assistant bot!
> hello
How can I help you?
> add Taras 0975551234
Contact added.
> add Alex 234abc
Phone must contain digits only.
> all
┌───────┬────────────┐
│ Name  │ Phone      │
├───────┼────────────┤
│ Taras │ 0975551234 │
└───────┴────────────┘
> exit
Good bye!
```

---

## Спільні пакети

- [`console_ui`](console_ui/) — кольорові принтери (`print_success`, `print_warning`, `print_error`, `print_info`, `print_title`) і базові ANSI-кольори в [`console_ui/colors.py`](console_ui/colors.py).
- [`file_reader.py`](file_reader.py) — централізоване читання текстових файлів із діагностикою `FileNotFoundError` / `PermissionError`.
