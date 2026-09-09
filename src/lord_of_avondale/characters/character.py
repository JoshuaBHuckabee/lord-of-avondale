"""
Character definition for the RPG
"""

from dataclasses import dataclass

from lord_of_avondale.utils.colors import Colors, color

@dataclass
class Character:
    """
    Represents a player character or NPC.

    This class contains the basic attributes and behavior shared
    by characters
    """

    name: str
    level: int = 1
    health: int = 100
    max_health: int = 100
    strength: int = 10
    defense: int = 10

    def is_alive(self) -> bool:
        """Return True if the character still has health."""
        return self.health > 0

    def heal(self, amount: int) -> None:
        """Restore health without exceeding max health."""
        self.health = min(self.health + amount, self.max_health)

    def take_damage(self, amount: int) -> None:
        """
        Reduce health by the specified amount.
        
        Health cannot fall below zero.
        """
        self.health = max(0, self.health - amount)

    def status(self) -> str:
        """
        Return a nicely formatted character status display.
        """

        health_color = (
            Colors.GREEN
            if self.health > self.max_health * 0.5
            else Colors.YELLOW
            if self.health > self.max_health * 0.2
            else Colors.RED
        )

        return (
            f"{Colors.BOLD}{self.name}{Colors.RESET}\n"
            f"Level: {self.level}\n"
            f"Health: "
            f"{color(f'{self.health}/{self.max_health}', health_color)}\n"
            f"Strength: {self.strength}\n"
            f"Defense: {self.defense}\n"
        )
