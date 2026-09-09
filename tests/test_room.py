"""
Tests for the Room class.
"""

import pytest

from lord_of_avondale.world.room import Room
from lord_of_avondale.npcs.npc import NPC

def test_room_stores_name_and_description() -> None:
    room = Room(
        name="Entrance",
        description="A dark entrance.",
    )

    assert room.name == "Entrance"
    assert room.description == "A dark entrance."

def test_room_has_no_exits_by_default() -> None:
    room = Room(
        name="Entrance",
        description="A dark entrance.",
    )

    assert room.exits == {}

def test_add_exit_connects_rooms() -> None:
    entrance = Room(
        name="Entrance",
        description="A dark entrance.",
    )

    hall = Room(
        name="Hall",
        description="A long hallway.",
    )

    entrance.add_exit("north", hall)

    assert entrance.get_exit("north") is hall

def test_directions_are_case_insensitive() -> None:
    entrance = Room(
        name="Entrance",
        description="A dark entrance.",
    )
    hall = Room(
        name="Hall",
        description="A long hallway.",
    )

    entrance.add_exit("NORTH", hall)

    assert entrance.get_exit("north") is hall
    assert entrance.get_exit("North") is hall


def test_missing_exit_returns_none() -> None:
    room = Room(
        name="Entrance",
        description="A dark entrance.",
    )

    assert room.get_exit("north") is None


def test_empty_direction_raises_error() -> None:
    room = Room(
        name="Entrance",
        description="A dark entrance.",
    )
    destination = Room(
        name="Hall",
        description="A long hallway.",
    )

    with pytest.raises(ValueError):
        room.add_exit("", destination)


def test_describe_includes_room_information() -> None:
    room = Room(
        name="Entrance",
        description="A dark entrance.",
    )

    description = room.describe()

    assert "Entrance" in description
    assert "A dark entrance." in description
    assert "There are no obvious exits." in description


def test_describe_includes_available_exits() -> None:
    entrance = Room(
        name="Entrance",
        description="A dark entrance.",
    )
    hall = Room(
        name="Hall",
        description="A long hallway.",
    )

    entrance.add_exit("north", hall)
    entrance.add_exit("east", hall)

    description = entrance.describe()

    assert "Exits: east, north" in description

def test_describe_includes_npcs() -> None:
    room = Room(
        name="Entrance",
        description="A dark entrance.",
    )

    npc = NPC(
        name="Old Hermit",
        description="An old man sits quietly.",
        current_room=room,
    )

    room.npcs.append(npc)

    description = room.describe()

    assert "You see: Old Hermit" in description