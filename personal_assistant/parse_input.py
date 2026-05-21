from .commands import Command
from .exceptions import EmptyInputError, UnknownCommandError


def parse_input(raw_input: str) -> tuple[Command, list[str]]:
    parts = raw_input.strip().split()
    if not parts:
        raise EmptyInputError("Empty input. Please type a command.")

    command_str = parts[0].lower()
    args = parts[1:]

    try:
        command = Command(command_str)
    except ValueError as e:
        raise UnknownCommandError(command_str) from e

    return command, args
