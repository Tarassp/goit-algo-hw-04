from .colors import RED, GREEN, YELLOW, BLUE, CYAN, BOLD, RESET


def print_error(message):
    for line in message.splitlines():
        print(f"{RED}{BOLD}{line}{RESET}")


def print_success(message):
    for line in message.splitlines():
        print(f"{GREEN}{BOLD}{line}{RESET}")


def print_success_items(items):
    for item in items:
        print_success(str(item))


def print_warning(message):
    for line in message.splitlines():
        print(f"{YELLOW}{BOLD}{line}{RESET}")


def print_info(message):
    for line in message.splitlines():
        print(f"{BLUE}{BOLD}{line}{RESET}")


def print_title(title):
    border = "─" * (len(title) + 4)
    print()
    print(f"{CYAN}{BOLD}┌{border}┐{RESET}")
    print(f"{CYAN}{BOLD}│  {title}  │{RESET}")
    print(f"{CYAN}{BOLD}└{border}┘{RESET}")
