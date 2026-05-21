from collections.abc import Callable

from .commands import Command
from .exceptions import ContactNotFoundError, ExitSignal, InvalidArgsError
from .formatters import format_contacts_table

type HandlerType = Callable[[list[str]], str | None]


def make_handlers() -> dict[Command, HandlerType]:
    contacts: dict[str, str] = {}

    def handle_hello(args: list[str]) -> str:
        return "How can I help you?"

    def handle_add(args: list[str]) -> None:
        if len(args) != 2:
            raise InvalidArgsError("Give me name and phone please.")
        name, phone = args
        if not phone.isdigit():
            raise InvalidArgsError("Phone must contain digits only.")
        contacts[name] = phone

    def handle_change(args: list[str]) -> None:
        if len(args) != 2:
            raise InvalidArgsError("Give me name and new phone please.")
        name, phone = args
        if name not in contacts:
            raise ContactNotFoundError(name)
        if not phone.isdigit():
            raise InvalidArgsError("Phone must contain digits only.")
        contacts[name] = phone

    def handle_phone(args: list[str]) -> str:
        if len(args) != 1:
            raise InvalidArgsError("Give me name please.")
        [name] = args
        if name not in contacts:
            raise ContactNotFoundError(name)
        return contacts[name]

    def handle_all(args: list[str]) -> str:
        if not contacts:
            return "Contacts list is empty."
        return format_contacts_table(contacts)

    def handle_exit(args: list[str]) -> None:
        raise ExitSignal()

    return {
        Command.HELLO: handle_hello,
        Command.ADD: handle_add,
        Command.CHANGE: handle_change,
        Command.PHONE: handle_phone,
        Command.ALL: handle_all,
        Command.EXIT: handle_exit,
        Command.CLOSE: handle_exit,
    }
