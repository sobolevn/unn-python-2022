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
    """
    This function is used to create a field at the very start of the game.

    :return: list with 16 randomly shuffled tiles,
        one of which is a empty space.
    """
    field = list(range(0, 16))
    random.shuffle(field)
    seed = random.randint(0, 16)
    for i, elem in enumerate(field):
        if elem == seed:
            field[i] = EMPTY_MARK

    return field
    pass


def print_field(field):
    """
    This function prints field to user.

    :param field: current field state to be printed.
    :return: None
    """
    for i in range(0, 16):
        print(field[i], end=' ')
        if (i + 1) % 4 == 0:
            print('', end='\n')
    pass


def is_game_finished(field):
    """
    This function checks if the game is finished.

    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    if field[15] != 'x':
        return False
    for i in range(0, 15):
        if (field[i] > field[i + 1]):
            return False
    return True
    pass


def perform_move(field, key):
    """
    Moves empty-tile inside the field.

    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move)
        or `None` if the move can't me done.
    """
    index = field.index('x')
    if 0 <= index + MOVES[key] <= 15:
        tmp = field[index]
        field[index] = field[index + MOVES[key]]
        field[index + MOVES[key]] = tmp
        return field
    else:
        return None
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

    key = input('Ход пользователя: ')
    if key not in MOVES:
        raise ValueError("")
    return key
    pass


def main():
    """
    The main function. It starts when the program is called.

    It also calls other functions.
    :return: None
    """
    field1 = shuffle_field()
    print_field(field1)
    pass


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    main()
