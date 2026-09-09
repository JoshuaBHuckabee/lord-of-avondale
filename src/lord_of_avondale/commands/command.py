"""
Command definitions for the game.
"""

from collections.abc import Callable

from lord_of_avondale.commands.context import GameContext
from lord_of_avondale.commands.result import CommandResult


CommandHandler = Callable[
    [GameContext, list[str]],
    CommandResult,
]
