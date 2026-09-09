"""
Tests for the world loader.
"""

from pathlib import Path

from lord_of_avondale.world.world_loader import load_world

DUNGEON_PATH = (
    Path(__file__).parent.parent
    / "src"
    / "lord_of_avondale"
    / "data"
    / "dungeons"
    / "forgotten_dungeon.json"
)

def test_load_world():
    rooms, start_room = load_world(DUNGEON_PATH)

    assert start_room == "entrance"
    assert len(rooms) == 5


def test_room_data():
    rooms, _ = load_world(DUNGEON_PATH)

    entrance = rooms["entrance"]

    assert entrance.name == "Dungeon Entrance"
    assert "north" in entrance.exits


def test_room_connections():
    rooms, _ = load_world(DUNGEON_PATH)

    entrance = rooms["entrance"]
    hall = rooms["hall"]
    chamber = rooms["chamber"]

    assert entrance.get_exit("north") is hall
    assert hall.get_exit("east") is chamber
    assert chamber.get_exit("west") is hall

