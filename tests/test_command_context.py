"""
Tests for the command game context.
"""

from lord_of_avondale.characters.character import Character
from lord_of_avondale.commands.context import GameContext
from lord_of_avondale.world.room import Room


def test_game_context_stores_player_and_room() -> None:
    player = Character(name="Aragorn")
    room = Room(
        name="Entrance",
        description="A dark entrance.",
    )

    context = GameContext(
        player=player,
        current_room=room,
    )

    assert context.player is player
    assert context.current_room is room
