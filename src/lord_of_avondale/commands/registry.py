"""
Command registry for the game.
"""

from lord_of_avondale.commands.command import CommandHandler

class CommandRegistry:
    """Stores command handlers by command name."""

    def __init__(self) -> None:
        self._commands: dict[str, CommandHandler] = {}

    def register(
        self, 
        name: str, 
        handler: CommandHandler,
        aliases: list[str] | None = None,
    ) -> None:
        """Register a command handler under a command name."""
        name = name.strip().lower()

        if not name: 
            raise ValueError("Command name cannot be empty.")

        self._commands[name] = handler

        for alias in aliases or []:
            alias = alias.strip().lower()

            if not alias: 
                raise ValueError("Command alias cannot be empty.")

            self._commands[alias] = handler

    def get(self, name: str) -> CommandHandler | None:
        """Return the handler for a command, if registered."""
        name = name.strip().lower()
        return self._commands.get(name)