"""
Tests for the examine command.
"""

from lord_of_avondale.characters.character import Character
from lord_of_avondale.commands.context import GameContext
from lord_of_avondale.commands.examine import examine
from lord_of_avondale.world.room import Room
from lord_of_avondale.npcs.npc import NPC


def test_examine_npc_returns_description() -> None:
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

    player = Character(name="Aragorn")

    context = GameContext(
        player=player,
        current_room=room,
    )

    result = examine(context, ["old", "hermit"])

    assert result.message == npc.description
    assert result.continue_game is True


def test_examine_unknown_npc_returns_message() -> None:
    room = Room(
        name="Entrance",
        description="A dark entrance.",
    )

    player = Character(name="Aragorn")

    context = GameContext(
        player=player,
        current_room=room,
    )

    result = examine(context, ["goblin"])

    assert result.message == "You don't see that here."
    assert result.continue_game is True