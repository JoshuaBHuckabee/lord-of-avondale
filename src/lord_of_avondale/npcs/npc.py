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

    def move_to(self, room: Room) -> None:
        """Move the NPC to another room."""

        if self in self.current_room.npcs:
            self.current_room.npcs.remove(self)

        room.npcs.append(self)
        self.current_room = room