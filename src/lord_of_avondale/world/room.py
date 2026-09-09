"""
Room definitions for the game world.
"""

from dataclasses import dataclass, field

@dataclass
class Room:
    """
    Represents a location in the game world.
    
    exits maps a direction to another Room.

    Example:

        room.exits["north"] = another_room
    """

    name: str
    description: str

    exits: dict[str, "Room"] = field(default_factory=dict)

    def add_exit(self, direction: str, room: "Room") -> None:
        """Connect this room to another room."""
        self.exits[direction] = room

    def get_exit(self, direction: str) -> "Room | None":
        """Return the room in the requested direction, if one exists."""
        return self.exits.get(direction)

    def describe(self) -> str:
        """Return a description suitable for displaying to the player."""

        output = [
            f"\n{self.name}",
            "-" * len(self.name),
            self.description,
        ]

        if self.exits:
            directions = ", ".join(sorted(self.exits))
            output.append(f"\nExits: {directions}")
        else:
            output.append("\nThere are no obvious exits.")

        return "\n".join(output)