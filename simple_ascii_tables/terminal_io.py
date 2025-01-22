"""Get info about the current terminal window/screen buffer."""

import shutil

DEFAULT_HEIGHT = 24
DEFAULT_WIDTH = 79


def terminal_size():
    size = shutil.get_terminal_size((DEFAULT_WIDTH, DEFAULT_HEIGHT))
    return size.columns, size.lines

