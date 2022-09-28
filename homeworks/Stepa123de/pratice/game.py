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
    This function is used to create a field at the every start of the game.

    :return: list with 16 randomly shuffled tiles,
        one of which is a empty space.
    """

    list = [];

    for i in range(15):
        list.append(i);

    list.append(EMPTY_MARK);

    for i in range(100):
        perform_move(list, random.choice(['w','a','s','d']))

    return list


def print_field(field):
    """
    This function prints field to user.

    :param field: current field state to be printed.
    :return: None
    """

    index = 0;
    print(field[0:4])
    print(field[4:8])
    print(field[8:12])
    print(field[12:])

    return None


def is_game_finished(field):
    if (field.index('x') != len(field)-1):
        return False

    for i in range(len(field)-1):
        if (field[i]>field[i+1]):
            return False

    return True;


def perform_move(field, key):
    """
    Moves empty-tile inside the field.

    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move)
        or `None` if the move can't me done.
    """

    truekey = MOVES.get(key);
    posX = field.index('x')
    newX = posX + truekey;

    if truekey == 1:
        if (newX < 16 and newX%4!=0):
            field[posX],field[newX] = field[newX],field[posX];
            return field
    elif truekey == -1:
        if (newX > -1 and (newX+1)%4!=0 ):
            field[posX], field[newX] = field[newX], field[posX];
            return field
    elif truekey == 4:
        if (newX < 16):
            field[posX], field[newX] = field[newX], field[posX];
            return field
    elif truekey == -4:
        if (newX > -1):
            field[posX], field[newX] = field[newX], field[posX];
            return field


    return None


def handle_user_input():
    """
    Handles user input.

    List of accepted moves:


    :return: <str> current move.
    """

    MYMOVES = {
        "up" :'w' ,
        "down" :'s' ,
        "left" :'a' ,
        "right" :'d' ,
    }

    a = input();

    return MYMOVES.get(a);


def main():
    """
    The main function. It starts when the program is called.

    It also calls other functions.
    :return: None
    """

    field = shuffle_field();
    while(is_game_finished(field) == False):
        print_field(field)
        perform_move(field,handle_user_input())

    return None


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    main()
