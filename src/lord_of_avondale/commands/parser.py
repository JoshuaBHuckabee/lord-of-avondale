"""Utilities for parsing player commands."""

DIRECTION_ALIASES = {
    "n": "north",
    "s": "south",
    "e": "east",
    "w": "west",
}

def parse_command(text: str) -> tuple[str, list[str]]:
    """
    Parse raw player input into a command and its arguments.

    Direction aliases are converted to their full direction name.
    """

    parts = text.strip().lower().split()

    if not parts:
        return "", []

    command = DIRECTION_ALIASES.get(parts[0], parts[0])
    arguments = parts[1:]

    return command, arguments