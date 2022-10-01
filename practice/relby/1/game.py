# `random` module is used to shuffle field, see:
# https://docs.python.org/3/library/random.html#random.shuffle
import random
import sys
import termios
import tty

from typing import Final

# Empty tile, there's only one empty cell on a field:
EMPTY_MARK: Final = 'x'

# Dictionary of possible moves if a form of:
# key -> (dy, dx) to move the empty tile on a field.
MOVES: Final = {
    'w': (+1, 0),
    's': (-1, 0),
    'a': (0, +1),
    'd': (0, -1),
}

# Make an alias to field
Field = list[list[int]]


# Helper functions
def field_from_flat_field(flat_field: list[int], size: int) -> Field:
    """
    This function returns field from flat_field.

    (flat_field is one dimensional list, and field is two dimensional)
    """
    field = []
    for ind in range(size):
        field_slice = slice(ind*size, ind*size + size)
        field.append(flat_field[field_slice])
    return field


def deep_copy_field(field: Field) -> Field:
    return [row[:] for row in field]


# Consts
FIELD_SIZE: Final = 4
EMPTY_CELL: Final = FIELD_SIZE**2 - 1
WINNING_FIELD: Final = field_from_flat_field(
    list(range(FIELD_SIZE**2)),
    FIELD_SIZE,
)

PADDING: Final = len(str(EMPTY_CELL)) + 1
# This should grow depending on FIELD_SIZE
SHUFFLE_ITERATIONS: Final = FIELD_SIZE*1000


# Field functions
def shuffle_field() -> Field:
    """
    This function is used to create a field at the very start of the game.

    :return: list with 16 randomly shuffled tiles,
        one of which is a empty space.
    """
    field = deep_copy_field(WINNING_FIELD)
    for _ in range(SHUFFLE_ITERATIONS):
        while True:
            move = random.choice(list(MOVES.keys()))
            new_field = perform_move(field, move)
            if new_field is not None:
                break
        field = new_field
    return field


def print_field(field: Field) -> None:
    """
    This function prints field to user.

    :param field: current field state to be printed.
    :return: None
    """
    for row in field:
        for cell in row:
            if cell == EMPTY_CELL:
                cell_to_render = EMPTY_MARK
            else:
                cell_to_render = str(cell + 1)
            sys.stdout.write(cell_to_render.rjust(PADDING))
        sys.stdout.write('\n')


def reprint_field(field: Field) -> None:
    sys.stdout.write('\x1b[{0}A'.format(FIELD_SIZE))
    sys.stdout.write('\x1b[{0}D'.format(FIELD_SIZE*PADDING))
    print_field(field)


def is_game_finished(field: Field) -> bool:
    """
    This function checks if the game is finished.

    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    return field == WINNING_FIELD


def perform_move(field: Field, key: str) -> Field | None:
    """
    Moves empty-tile inside the field.

    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move)
        or `None` if the move can't me done.
    """
    move = MOVES.get(key)
    if move is None:
        return None

    empty_cell_pos = None
    for y, row in enumerate(field):
        for x, cell in enumerate(row):
            if EMPTY_CELL == cell:
                empty_cell_pos = y, x
    assert empty_cell_pos is not None

    y1, x1 = empty_cell_pos

    dy, dx = move
    y2, x2 = (y1 + dy, x1 + dx)

    if y2 < 0 or y2 >= FIELD_SIZE:
        return None
    if x2 < 0 or x2 >= FIELD_SIZE:
        return None

    new_field = deep_copy_field(field)
    new_field[y1][x1], new_field[y2][x2] = new_field[y2][x2], new_field[y1][x1]
    return new_field


# Terminal magic (works only on Unix-like systems)
# I use this to render each mutation to the field
# on top of the previous rendered field (so basically it re-renders the field,
# so the terminal doesn't get littered with a bunch of symbols)
def init_term():
    fd = sys.stdin.fileno()
    oldt = termios.tcgetattr(fd)
    newt = oldt.copy()
    newt[tty.LFLAG] &= ~(termios.ICANON | termios.ECHO)
    termios.tcsetattr(fd, termios.TCSANOW, newt)
    return fd, oldt


def revert_term(fd, oldt):
    termios.tcsetattr(fd, termios.TCSANOW, oldt)


def main() -> None:
    """
    The main function. It starts when the program is called.

    It also calls other functions.
    :return: None
    """
    fd, oldt = init_term()

    field = shuffle_field()
    print_field(field)
    while True:
        if is_game_finished(field):
            print('You have won!')
            break
        key = sys.stdin.read(1)
        if key == 'q':
            break
        new_field = perform_move(field, key)
        if new_field is not None:
            field = new_field
            reprint_field(field)

    revert_term(fd, oldt)


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    main()
