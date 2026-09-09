"""
Look command.
"""

from lord_of_avondale.commands.context import GameContext


def look(context: GameContext, arguments: list[str]) -> str:
    """Return a description of the player's current room."""
    return context.current_room.describe()