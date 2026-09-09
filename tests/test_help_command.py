"""
Tests for the help command.
"""

from lord_of_avondale.characters.character import Character
from lord_of_avondale.commands.context import GameContext
from lord_of_avondale.commands.help import help_command
from lord_of_avondale.world.room import Room

def test_help_returns_available_commands() -> None:
    player = Character(name="Aragorn")
    room = Room(
        name="Dungeon Entrance",
        description="A dark entrance.",
    )

    context = GameContext(
        player=player,
        current_room=room,
    )

    result = help_command(context, [])

    assert "north / n" in result.message
    assert "south / s" in result.message
    assert "east  / e" in result.message
    assert "west  / w" in result.message
    assert "look" in result.message
    assert "status" in result.message
    assert "help" in result.message
    assert "quit" in result.message
    assert result.continue_game is True