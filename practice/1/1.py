# `random` module is used to shuffle field, see:
# https://docs.python.org/3/library/random.html#random.shuffle
from operator import is_
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
    data = [i+1 for i in range (16)]
    data[15] = EMPTY_MARK
    for move in range(100):
        data = perform_move(data,  random.choice("wasd"))
    return data


def print_field(field):
    """
    This function prints field to user.

    :param field: current field state to be printed.
    :return: None
    """

    print(field[0:4])
    print(field[4:8])
    print(field[8:12])
    print(field[12:17])
    pass


def is_game_finished(field):
    """
    This function checks if the game is finished.

    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    data = [i+1 for i in range (16)]
    data[15] = EMPTY_MARK
    if field == data:
        return True
    return False


def perform_move(field, key):
    """
    Moves empty-tile inside the field.

    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move)
        or `None` if the move can't me done.
    """
    index = field.index(EMPTY_MARK) 
    if index + MOVES[key] <= 15 and index + MOVES[key] >= 0:
        if(key == 'a' or key == 'd'):
            if (index)//4 == (index + MOVES[key])//4:
                field[index], field[index + MOVES[key]] = field[index + MOVES[key]], field[index]
        else:
            field[index], field[index + MOVES[key]] = field[index + MOVES[key]], field[index]
    return field



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
    key = str(input())
    return key


def main():
    """
    The main function. It starts when the program is called.

    It also calls other functions.
    :return: None
    """

    map = shuffle_field()
    print_field(map)


    while(not is_game_finished(map)):
        map = perform_move(map, handle_user_input())
        print_field(map)
    pass

if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    main()