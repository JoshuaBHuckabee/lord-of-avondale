"""
Tests for the quit command.
"""

from lord_of_avondale.characters.character import Character
from lord_of_avondale.commands.context import GameContext
from lord_of_avondale.commands.quit import quit_command
from lord_of_avondale.world.room import Room


def test_quit_command_ends_game() -> None:
    player = Character(name="Aragorn")
    room = Room(
        name="Entrance",
        description="A dark entrance.",
    )

    context = GameContext(
        player=player,
        current_room=room,
    )

    result = quit_command(context, [])

    assert result.message == "\nFarewell, adventurer."
    assert result.continue_game is False