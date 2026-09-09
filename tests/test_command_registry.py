"""
Tests for the command registry.
"""

from lord_of_avondale.commands.registry import CommandRegistry


def test_registry_starts_empty() -> None:
    registry = CommandRegistry()

    assert registry.get("look") is None


def test_register_command() -> None:
    registry = CommandRegistry()

    def look_command() -> None:
        pass

    registry.register("look", look_command)

    assert registry.get("look") is look_command


def test_command_names_are_case_insensitive() -> None:
    registry = CommandRegistry()

    def look_command() -> None:
        pass

    registry.register("LOOK", look_command)

    assert registry.get("look") is look_command


def test_register_command_strips_whitespace() -> None:
    registry = CommandRegistry()

    def look_command() -> None:
        pass

    registry.register("  look  ", look_command)

    assert registry.get("look") is look_command

def test_register_command_with_alias() -> None:
    registry = CommandRegistry()

    def look_command() -> None:
        pass

    registry.register("look", look_command, aliases=["l"])

    assert registry.get("look") is look_command
    assert registry.get("l") is look_command


def test_aliases_are_case_insensitive() -> None:
    registry = CommandRegistry()

    def look_command() -> None:
        pass

    registry.register("look", look_command, aliases=["L"])

    assert registry.get("l") is look_command


def test_aliases_are_stripped() -> None:
    registry = CommandRegistry()

    def look_command() -> None:
        pass

    registry.register("look", look_command, aliases=["  l  "])

    assert registry.get("l") is look_command
