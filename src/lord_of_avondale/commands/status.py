"""
Status command.
"""

from lord_of_avondale.commands.context import GameContext

def status(context: GameContext, arguments: list[str]) -> str:
    """Return the player's current status."""
    return context.player.status()