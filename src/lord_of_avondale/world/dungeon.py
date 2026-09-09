"""
Creates the game's initial dungeon.
"""

from lord_of_avondale.world.room import Room

def create_dungeon() -> Room:
    """
    Contstruct the starting dungeon.

    Returns:
        The room where the player should begin.
    """

    entrance = Room(
        name="Dungeon Entrance",
        description=(
            "Cold air drifts through the ancient stone passage. "
            "A narrow stairway leads deeper into darkness."
        ),
    )

    hall = Room(
        name="The Long Hall",
        description=(
            "Torches flicker weakly along the walls."
            "The stone beneath your feet is worn smooth by centuries "
            "of travelers."
        ),
    )

    chamber = Room(
        name="Goblin's Chamber",
        description=(
            "A foul-smelling chamber filled with broken crates and "
            "old bones. Something has been living here."
        ),
    )

    crossroads = Room(
        name="The Crossroads",
        description=(
            "Four ancient passages meet here. "
            "The air is strangely still."
        ),
    )

    treasure_room = Room(
        name="Forgotten Treasury",
        description=(
            "Dust-covered stone chests line the walls. "
            "Whatever treasures once filled this room are long gone."
        ),
    )

    # Connect the rooms together.

    entrance.add_exit("north", hall)

    hall.add_exit("south", entrance)
    hall.add_exit("east", chamber)
    hall.add_exit("north", crossroads)

    chamber.add_exit("west", hall)

    crossroads.add_exit("south", hall)
    crossroads.add_exit("east", treasure_room)

    treasure_room.add_exit("west", crossroads)

    return entrance
    

    