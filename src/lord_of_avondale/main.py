"""
Entry point for the RPG.
"""

from pathlib import Path

from lord_of_avondale.characters.character import Character
from lord_of_avondale.commands.parser import parse_command
from lord_of_avondale.utils.colors import Colors, color
from lord_of_avondale.world.world_loader import load_world


def print_help() -> None:
    """Display the commands currently available to the player."""

    print(
        """
Commands
--------
north / n
south / s
east  / e
west  / w

look
status
help
quit
"""
    )


def main() -> None:
    """Start the game."""

    print(
        color(
            "\n====================================\n"
            "        THE FORGOTTEN DUNGEON\n"
            "====================================",
            Colors.CYAN,
        )
    )

    name = input("\nWhat is your name, adventurer? ").strip()

    if not name:
        name = "Adventurer"

    player = Character(name=name)
    dungeon_path = (
        Path(__file__).parent
        / "data"
        / "dungeons"
        / "forgotten_dungeon.json"
    )

    rooms, start_room = load_world(dungeon_path)
    current_room = rooms[start_room]

    print(
        f"\nWelcome, "
        f"{color(player.name, Colors.YELLOW)}."
    )

    print(current_room.describe())

    print_help()

    while player.is_alive():
        command, arguments = parse_command(
            input(
                 f"\n{color(player.name, Colors.GREEN)} > "
            )
        )

        if command in {"quit", "exit"}:
            print("\nFarewell, adventurer.")
            break

        if command in {"help", "?"}:
            print_help()
            continue

        if command in {"look", "l"}:
            print(current_room.describe())
            continue

        if command in {"status", "stats"}:
            print()
            print(player.status())
            continue

        direction = command

        destination = current_room.get_exit(direction)

        if destination is None:
            print(
                color(
                    "You cannot go that way.",
                    Colors.RED,
                )
            )
            continue

        current_room = destination

        print(current_room.describe())


if __name__ == "__main__":
    main()
