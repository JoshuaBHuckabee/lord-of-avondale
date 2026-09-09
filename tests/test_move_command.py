"""
Tests for the movement commands.
"""

from lord_of_avondale.characters.character import Character
from lord_of_avondale.commands.context import GameContext
from lord_of_avondale.commands.move import east, north, south, west
from lord_of_avondale.world.room import Room


def create_context() -> tuple[GameContext, Room, Room]:
    """Create a simple two-room world for movement tests."""

    player = Character(name="Aragorn")

    entrance = Room(
        name="Entrance",
        description="A dark entrance.",
    )

    hall = Room(
        name="Hall",
        description="A long hallway.",
    )

    context = GameContext(
        player=player,
        current_room=entrance,
    )

    return context, entrance, hall


def test_move_north_changes_current_room() -> None:
    context, entrance, hall = create_context()

    entrance.add_exit("north", hall)

    result = north(context, [])

    assert context.current_room is hall
    assert result.message == hall.describe()
    assert result.continue_game is True


def test_move_to_invalid_direction() -> None:
    context, entrance, _ = create_context()

    result = north(context, [])

    assert context.current_room is entrance
    assert result.message == "You cannot go that way."
    assert result.continue_game is True


def test_move_south() -> None:
    context, entrance, hall = create_context()

    hall.add_exit("south", entrance)
    context.current_room = hall

    result = south(context, [])

    assert context.current_room is entrance
    assert result.message == entrance.describe()


def test_move_east() -> None:
    context, entrance, hall = create_context()

    entrance.add_exit("east", hall)

    result = east(context, [])

    assert context.current_room is hall
    assert result.message == hall.describe()


def test_move_west() -> None:
    context, entrance, hall = create_context()

    hall.add_exit("west", entrance)
    context.current_room = hall

    result = west(context, [])

    assert context.current_room is entrance
    assert result.message == entrance.describe()