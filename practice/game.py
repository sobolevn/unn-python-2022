# `random` module is used to shuffle field, see:
# https://docs.python.org/3/library/random.html#random.shuffle
import random

# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of:
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    field = []
    for i in range(15):
        field.append(random.randint(1,15))
    field.append(EMPTY_MARK)
    random.shuffle(field)
    return field


def print_field(field):
    i = 0
    j = 0
    for i in range(4):
        print(field[j:j+4])
        j+=4
    return field


def is_game_finished(field):
    if field[15] != EMPTY_MARK:
        return False
    for i in range(14):
        if field[i] != field[i+1]:
            return False
    return True



def perform_move(field, key):
    """
    Moves empty-tile inside the field.

    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move)
        or `None` if the move can't me done.
    """
    pass


def handle_user_input():
    """
    Handles user input.

    List of accepted moves:
        'w' - up,
        's' - down,
        'a' - left,
        'd' - right

    :return: <str> current move.
    """
    pass


def main():
    """
    The main function. It starts when the program is called.

    It also calls other functions.
    :return: None
    """
    pass


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    main()
