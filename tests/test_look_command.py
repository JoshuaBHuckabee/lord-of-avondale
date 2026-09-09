"""
Tests for the look command.
"""

from lord_of_avondale.characters.character import Character
from lord_of_avondale.commands.context import GameContext
from lord_of_avondale.commands.look import look
from lord_of_avondale.world.room import Room


def test_look_returns_current_room_description() -> None:
    player = Character(name="Aragorn")
    room = Room(
        name="Dungeon Entrance",
        description="A dark entrance.",
    )

    context = GameContext(
        player=player,
        current_room=room,
    )

    result = look(context, [])

    assert result.message == room.describe()
    assert result.continue_game is True