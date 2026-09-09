"""
Movement commands.
"""

from lord_of_avondale.commands.context import GameContext
from lord_of_avondale.commands.result import CommandResult


def _move(
    context: GameContext,
    direction: str,
) -> CommandResult:
    """Move the player in the requested direction."""

    destination = context.current_room.get_exit(direction)

    if destination is None:
        return CommandResult(
            message="You cannot go that way.",
        )

    context.current_room = destination

    return CommandResult(
        message=context.current_room.describe(),
    )


def north(
    context: GameContext,
    arguments: list[str],
) -> CommandResult:
    """Move north."""

    return _move(context, "north")


def south(
    context: GameContext,
    arguments: list[str],
) -> CommandResult:
    """Move south."""

    return _move(context, "south")


def east(
    context: GameContext,
    arguments: list[str],
) -> CommandResult:
    """Move east."""

    return _move(context, "east")


def west(
    context: GameContext,
    arguments: list[str],
) -> CommandResult:
    """Move west."""

    return _move(context, "west")
