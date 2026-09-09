"""
Tests for the main game entry point.
"""

from lord_of_avondale.commands.context import GameContext
from lord_of_avondale.commands.registry import CommandRegistry
from lord_of_avondale.world.room import Room
from lord_of_avondale.characters.character import Character
from lord_of_avondale.main import execute_command


def test_execute_command_returns_handler_result() -> None:
    player = Character(name="Aragorn")
    room = Room(
        name="Entrance",
        description="A dark entrance.",
    )

    context = GameContext(
        player=player,
        current_room=room,
    )

    registry = CommandRegistry()

    def test_command(context: GameContext, arguments: list[str]) -> str:
        return "Command executed."

    registry.register("test", test_command)

    result = execute_command(
        registry,
        context,
        "test",
        [],
    )

    assert result == "Command executed."


def test_execute_unknown_command_returns_none() -> None:
    player = Character(name="Aragorn")
    room = Room(
        name="Entrance",
        description="A dark entrance.",
    )

    context = GameContext(
        player=player,
        current_room=room,
    )

    registry = CommandRegistry()

    result = execute_command(
        registry,
        context,
        "unknown",
        [],
    )

    assert result is None