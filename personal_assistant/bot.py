from enum import Enum

from console_ui import print_error, print_success, print_warning

from .commands import Command
from .exceptions import (
    ContactNotFoundError,
    EmptyInputError,
    ExitSignal,
    InvalidArgsError,
    UnknownCommandError,
)
from .handlers import HandlerType, make_handlers
from .parse_input import parse_input


class Severity(Enum):
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"


type CommandOutput = tuple[str, Severity]

SUCCESS_MESSAGES = {
    Command.ADD: "Contact added.",
    Command.CHANGE: "Contact updated.",
}


def process_command(
    raw: str, handlers: dict[Command, HandlerType]
) -> CommandOutput | None:
    """Run one command and return (message, severity) or None.

    Raises ExitSignal to terminate the main loop.
    """
    try:
        cmd, args = parse_input(raw)
    except (EmptyInputError, UnknownCommandError):
        return "Invalid command.", Severity.ERROR

    try:
        result = handlers[cmd](args)
    except ContactNotFoundError:
        return "Contact not found.", Severity.WARNING
    except InvalidArgsError as e:
        return str(e), Severity.WARNING

    if result is not None:
        return result, Severity.SUCCESS

    success_msg = SUCCESS_MESSAGES.get(cmd)
    if success_msg is None:
        return None
    return success_msg, Severity.SUCCESS


PRINTERS = {
    Severity.SUCCESS: print_success,
    Severity.WARNING: print_warning,
    Severity.ERROR: print_error,
}


def run():
    handlers = make_handlers()
    print("Welcome to the assistant bot!")

    while True:
        try:
            output = process_command(input("> "), handlers)
        except ExitSignal:
            print_success("Good bye!")
            break
        if output is None:
            continue
        message, severity = output
        PRINTERS[severity](message)
