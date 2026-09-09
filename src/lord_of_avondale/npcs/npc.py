"""
NPC definitions for the game.
"""

from dataclasses import dataclass

from lord_of_avondale.world.room import Room


@dataclass
class NPC:
    """
    Represents a non-player character in the game world.
    """

    name: str
    description: str
    current_room: Room
