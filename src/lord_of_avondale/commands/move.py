"""
Movement command.
"""

from lord_of_avondale.commands.context import GameContext
from lord_of_avondale.commands.result import CommandResult


def move(
    context: GameContext,
    arguments: list[str],
) -> CommandResult:
    """Move the player in the requested direction."""

    if not arguments:
        return CommandResult(
            message="Go where?",
        )

    direction = arguments[0]

    destination = context.current_room.get_exit(direction)

    if destination is None:
        return CommandResult(
            message="You cannot go that way.",
        )

    context.current_room = destination

    return CommandResult(
        message=context.current_room.describe(),
    )
