from lord_of_avondale.commands.parser import parse_command


def test_parse_direction() -> None:
    command, arguments = parse_command("north")

    assert command == "north"
    assert arguments == []


def test_parse_direction_alias() -> None:
    command, arguments = parse_command("n")

    assert command == "north"
    assert arguments == []


def test_parse_command_with_arguments() -> None:
    command, arguments = parse_command("look around")

    assert command == "look"
    assert arguments == ["around"]


def test_parse_command_is_case_insensitive() -> None:
    command, arguments = parse_command("NORTH")

    assert command == "north"
    assert arguments == []


def test_parse_command_strips_whitespace() -> None:
    command, arguments = parse_command("  north  ")

    assert command == "north"
    assert arguments == []


def test_parse_empty_command() -> None:
    command, arguments = parse_command("")

    assert command == ""
    assert arguments == []