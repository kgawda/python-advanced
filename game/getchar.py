import os

if os.name == "nt":  # Windows
    import msvcrt
else:
    import tty
    import termios
    import sys

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"


def getchar():
    """Returns a single character from standard input"""
    ch = ""
    if os.name == "nt":
        ch = msvcrt.getch()
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def getchar_arrow():
    """Returns a character from standard input:
      - single character
      - arrow name for up/down/left/right arrows
      - string representing other special keys
    """

    ch = getchar()
    if ch != "\x1b":
        return ch

    # Expecting special key, e.g. an arrow
    ch2 = getchar()
    ch3 = getchar()
    if ch2 == "[":
        if ch3 == "A":
            return UP
        if ch3 == "B":
            return DOWN
        if ch3 == "C":
            return RIGHT
        if ch3 == "D":
            return LEFT

    # Unknown key, return the whole code
    return ch + ch2 + ch3
