"""
Context shared by game commands.
"""

from dataclasses import dataclass

from lord_of_avondale.characters.character import Character
from lord_of_avondale.world.room import Room

@dataclass
class GameContext:
    """State available to command handlers."""

    player: Character
    current_room: Room