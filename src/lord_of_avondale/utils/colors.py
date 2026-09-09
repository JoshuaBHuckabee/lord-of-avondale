"""
ANSI color helpers.

Keeping colors in their own module mean the rest of the game doesn't
need to know how ANSI escape sequences work.
"""

class Colors:
    """ANSI escape sequences used by the game."""

    RESET = "\033[0m"

    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[337m"

    BOLD = "\033[1m"

def color(text: str, color_code: str) -> str:
    """
    Wrap text in an ANSI color code.

    Returns:
        str: _description_
    """
    return f"{color_code}{text}{Colors.RESET}"