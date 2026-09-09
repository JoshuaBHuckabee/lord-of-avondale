"""
Status command.
"""

from lord_of_avondale.commands.context import GameContext
from lord_of_avondale.commands.result import CommandResult

def status(
    context: GameContext,
    arguments: list[str],
) -> CommandResult:
    """Return the player's current status."""

    return CommandResult(
        message=context.player.status(),
    )