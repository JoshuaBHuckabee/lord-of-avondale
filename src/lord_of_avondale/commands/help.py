"""
Help command.
"""

from lord_of_avondale.commands.context import GameContext


def help_command(context: GameContext, arguments: list[str]) -> str:
    """Return the commands currently available to the player."""

    return """
Commands
--------
north / n
south / s
east  / e
west  / w

look
status
help
quit
"""
