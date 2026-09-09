"""
Examine command.
"""

from lord_of_avondale.commands.context import GameContext
from lord_of_avondale.commands.result import CommandResult


def examine(
    context: GameContext,
    arguments: list[str],
) -> CommandResult:
    """Examine an NPC in the player's current room."""

    if not arguments:
        return CommandResult(
            message="Examine what?",
        )

    target = " ".join(arguments).lower()

    for npc in context.current_room.npcs:
        if npc.name.lower() == target:
            return CommandResult(
                message=npc.description,
            )

    return CommandResult(
        message="You don't see that here.",
    )
