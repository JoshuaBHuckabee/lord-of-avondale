"""
Entry point for the RPG.
"""

from pathlib import Path

from lord_of_avondale.characters.character import Character
from lord_of_avondale.commands.parser import parse_command
from lord_of_avondale.commands.look import look
from lord_of_avondale.commands.move import north, south, east, west
from lord_of_avondale.commands.status import status
from lord_of_avondale.commands.help import help_command
from lord_of_avondale.commands.quit import quit_command
from lord_of_avondale.commands.registry import CommandRegistry
from lord_of_avondale.commands.context import GameContext
from lord_of_avondale.commands.result import CommandResult
from lord_of_avondale.utils.colors import Colors, color
from lord_of_avondale.world.world_loader import load_world

def execute_command(
    registry: CommandRegistry,
    context: GameContext,
    command: str,
    arguments: list[str],
) -> CommandResult | None:
    """Execute a registered command and return its output."""

    handler = registry.get(command)

    if handler is None:
        return None

    return handler(context, arguments)

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
    registry.register("help", help_command, aliases=["?"])
    registry.register("quit", quit_command, aliases=["exit"])
    registry.register("north", north, aliases=["n"])
    registry.register("south", south, aliases=["s"])
    registry.register("east", east, aliases=["e"])
    registry.register("west", west, aliases=["w"])

    print(
        f"\nWelcome, "
        f"{color(player.name, Colors.YELLOW)}."
    )

    print(context.current_room.describe())

    result = execute_command(
        registry,
        context,
        "help",
        [],
    )

    if result is not None and result.message:
        print(result.message)

    while player.is_alive():
        command, arguments = parse_command(
            input(
                 f"\n{color(player.name, Colors.GREEN)} > "
            )
        )

        result = execute_command(
            registry,
            context,
            command,
            arguments,
        )

        if result is not None:
            if result.message:
                print(result.message)

            if not result.continue_game:
                break

            continue

        print(
            color(
                "Unknown command.",
                Colors.RED,
            )
        )

if __name__ == "__main__":
    main()
