"""
Help command.
"""

from lord_of_avondale.commands.context import GameContext
from lord_of_avondale.commands.result import CommandResult


def help_command(
    context: GameContext,
    arguments: list[str],
) -> CommandResult:
    """Return the commands currently available to the player."""

    return CommandResult(
        message="""
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
    )