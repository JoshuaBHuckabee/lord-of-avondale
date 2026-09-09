"""
Quit command.
"""

from lord_of_avondale.commands.context import GameContext
from lord_of_avondale.commands.result import CommandResult


def quit_command(
    context: GameContext,
    arguments: list[str],
) -> CommandResult:
    """End the current game session."""

    return CommandResult(
        message="\nFarewell, adventurer.",
        continue_game=False,
    )