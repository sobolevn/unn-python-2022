# `random` module is used to shuffle field, see:
# https://docs.python.org/3/library/random.html#random.shuffle
from dataclasses import field
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
    field = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', EMPTY_MARK]
    random.shuffle(field)
    return field



def print_field(field):
    """
    This function prints field to user.

    :param field: current field state to be printed.
    :return: None
    """
    i = 0
    print("----------------------")
    for item in field:
        if(i % 4 == 0 and i != 0):
            print('|\n')
        print(f"| {item}", end=" ")
        i += 1
    print("|\n----------------------")
    


def is_game_finished(field):
    """
    This function checks if the game is finished.

    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    correct_field = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', EMPTY_MARK)
    if (correct_field == tuple(field)):
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
    temp = field.index(EMPTY_MARK)
    
    if (temp == 0 and (key == 'w' or key == 'a')):
        return None
    if (temp == 3 and (key == 'w' or key == 'd')):
        return None
    if (temp == 12 and (key == 's' or key == 'a')):
        return None
    if (temp == 15 and (key == 's' or key == 'd')):
        return None
    if ((temp == 1 or temp == 2) and key == 'w'):
        return None
    if ((temp == 4 or temp == 8) and key == 'a'):
        return None
    if ((temp == 13 or temp == 14) and key == 's'):
        return None
    if ((temp == 7 or temp == 11) and key == 'd'):
        return None    
    field[temp] = field[temp + MOVES[key]]
    field[temp + MOVES[key]] = EMPTY_MARK
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
    cur_move = input("Введите направление движения:\n\t 1) 'w' - up \n\t 2) 's' - down \n\t 3) 'a' - left \n\t 4) 'd' - right \n")
    return cur_move


def main():
    """
    The main function. It starts when the program is called.

    It also calls other functions.
    :return: None
    """
    field = shuffle_field()
    while(True):
        if(is_game_finished(field)):
            print("You are winner!")
            break
        print_field(field)
        cur_move = handle_user_input()
        perform_move(field, cur_move)

if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    main()
