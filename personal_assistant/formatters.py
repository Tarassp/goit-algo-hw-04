NAME_HEADER = "Name"
PHONE_HEADER = "Phone"


def format_contacts_table(contacts: dict[str, str]) -> str:
    name_width = max(len(NAME_HEADER), max(len(n) for n in contacts))
    phone_width = max(len(PHONE_HEADER), max(len(p) for p in contacts.values()))

    top    = f"┌─{'─' * name_width}─┬─{'─' * phone_width}─┐"
    header = f"│ {NAME_HEADER:<{name_width}} │ {PHONE_HEADER:<{phone_width}} │"
    sep    = f"├─{'─' * name_width}─┼─{'─' * phone_width}─┤"
    bottom = f"└─{'─' * name_width}─┴─{'─' * phone_width}─┘"

    rows = [
        f"│ {name:<{name_width}} │ {phone:<{phone_width}} │"
        for name, phone in contacts.items()
    ]

    return "\n".join([top, header, sep, *rows, bottom])
