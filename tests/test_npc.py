"""
Tests for the NPC class.
"""

from lord_of_avondale.npcs.npc import NPC
from lord_of_avondale.world.room import Room


def test_npc_stores_name_and_description() -> None:
    room = Room(
        name="Entrance",
        description="A dark entrance.",
    )

    npc = NPC(
        name="Old Hermit",
        description="An old man watches you silently.",
        current_room=room,
    )

    assert npc.name == "Old Hermit"
    assert npc.description == "An old man watches you silently."
    assert npc.current_room is room
