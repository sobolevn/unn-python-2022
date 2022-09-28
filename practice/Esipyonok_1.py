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
    field = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, EMPTY_MARK]
    field = random.sample(field,16)
    return field


def print_field(field):
    """
    This function prints field to user.

    :param field: current field state to be printed.
    :return: None
    """
    k = 0
    for step in range field:
        print (step)
        k += 1
        if k == 4
            print (/n)
    return None


def is_game_finished(field):
    """
    This function checks if the game is finished.

    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    ended = False
    if field == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, EMPTY_MARK]
        ended = True
    return ended


def perform_move(field, key):
    """
    Moves empty-tile inside the field.

    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move)
        or `None` if the move can't me done.
    """
    if """ условие """
    """ поменять местами х и цифру на месте, куда переносится х """
    return field
    else 
    print ('incorrect direction')
    return None


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
    shift = input ("Print _ for go to: 'w' - up, 's' - down, 'a' - left, 'd' - right")
    if shift == 'w' 
        return 'w'
    elif shift == 's' 
        return 's'
    elif shift == 'a' 
        return 'a'
    elif shift == 'd' 
        return 'd'
    else
        print('incorrect input')
        return None


def main():
    """
    The main function. It starts when the program is called.

    It also calls other functions.
    :return: None
    """
    shuffle_field()
    while True 
    print_field(field)
    handle_user_input()
    perform_move(field, key)
    if is_game_finished(field)
    break
    return None


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    main()
