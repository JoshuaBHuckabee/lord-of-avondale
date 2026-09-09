"""
Entry point for the RPG.
"""

from pathlib import Path

from lord_of_avondale.characters.character import Character
from lord_of_avondale.commands.parser import parse_command
from lord_of_avondale.commands.look import look
from lord_of_avondale.commands.status import status
from lord_of_avondale.commands.registry import CommandRegistry
from lord_of_avondale.commands.context import GameContext
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

    context = GameContext(
        player=player,
        current_room=rooms[start_room],
    )

    registry = CommandRegistry()
    registry.register("look", look, aliases=["l"])
    registry.register("status", status, aliases=["stats"])

    print(
        f"\nWelcome, "
        f"{color(player.name, Colors.YELLOW)}."
    )

    print(context.current_room.describe())

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

        handler = registry.get(command)

        if handler is not None:
            result = handler(context, arguments)

            if result:
                print(result)

            continue

        direction = command

        destination = context.current_room.get_exit(direction)

        if destination is None:
            print(
                color(
                    "You cannot go that way.",
                    Colors.RED,
                )
            )
            continue

        context.current_room = destination

        print(context.current_room.describe())


if __name__ == "__main__":
    main()
