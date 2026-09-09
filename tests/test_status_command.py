"""
Tests for the status command.
"""

from lord_of_avondale.characters.character import Character
from lord_of_avondale.commands.context import GameContext
from lord_of_avondale.commands.status import status
from lord_of_avondale.world.room import Room


def test_status_returns_player_status() -> None:
    player = Character(name="Aragorn")
    room = Room(
        name="Dungeon Entrance",
        description="A dark entrance.",
    )

    context = GameContext(
        player=player,
        current_room=room,
    )

    result = status(context, [])

    assert result == player.status()
