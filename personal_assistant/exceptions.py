class EmptyInputError(ValueError):
    pass


class UnknownCommandError(ValueError):
    pass


class InvalidArgsError(ValueError):
    pass


class ContactNotFoundError(KeyError):
    pass


class ExitSignal(Exception):
    """Signal to terminate the bot's main loop."""
    pass
