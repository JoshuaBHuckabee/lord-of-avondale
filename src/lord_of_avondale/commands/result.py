"""
Results returned by game commands.
"""

from dataclasses import dataclass


@dataclass
class CommandResult:
    """Represents the result of executing a command."""

    message: str | None = None
    continue_game: bool = True
