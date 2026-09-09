"""
Command definitions for the game.
"""

from collections.abc import Callable

from lord_of_avondale.commands.context import GameContext


CommandHandler = Callable[[GameContext, list[str]], str | None]