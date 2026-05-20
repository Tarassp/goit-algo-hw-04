from .colors import RED, GREEN, BOLD, RESET


def print_error(message):
    for line in message.splitlines():
        print(f"{RED}{BOLD}{line}{RESET}")


def print_success(message):
    for line in message.splitlines():
        print(f"{GREEN}{BOLD}{line}{RESET}")
