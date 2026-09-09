"""
Tests for the movement command.
"""

from lord_of_avondale.characters.character import Character
from lord_of_avondale.commands.context import GameContext
from lord_of_avondale.commands.move import move
from lord_of_avondale.world.room import Room


def test_move_changes_current_room() -> None:
    player = Character(name="Aragorn")

    entrance = Room(
        name="Entrance",
        description="A dark entrance.",
    )

    hall = Room(
        name="Hall",
        description="A long hallway.",
    )

    entrance.add_exit("north", hall)

    context = GameContext(
        player=player,
        current_room=entrance,
    )

    result = move(context, ["north"])

    assert context.current_room is hall
    assert result.message == hall.describe()
    assert result.continue_game is True


def test_move_to_invalid_direction() -> None:
    player = Character(name="Aragorn")

    room = Room(
        name="Entrance",
        description="A dark entrance.",
    )

    context = GameContext(
        player=player,
        current_room=room,
    )

    result = move(context, ["north"])

    assert context.current_room is room
    assert result.message == "You cannot go that way."
    assert result.continue_game is True


def test_move_without_direction() -> None:
    player = Character(name="Aragorn")

    room = Room(
        name="Entrance",
        description="A dark entrance.",
    )

    context = GameContext(
        player=player,
        current_room=room,
    )

    result = move(context, [])

    assert context.current_room is room
    assert result.message == "Go where?"
    assert result.continue_game is True
