"""
Look command.
"""

from lord_of_avondale.commands.context import GameContext
from lord_of_avondale.commands.result import CommandResult

def look(
    context: GameContext,
    arguments: list[str],
) -> CommandResult:
    """Return a description of the player's current room."""

    return CommandResult(
        message=context.current_room.describe(),
    )