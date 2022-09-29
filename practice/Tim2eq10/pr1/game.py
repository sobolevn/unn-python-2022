# `random` module is used to shuffle field, see:
# https://docs.python.org/3/library/random.html#random.shuffle
import random

from pkg_resources import empty_provider

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
    field = [x + 1 for x in range(15)]
    field.append(EMPTY_MARK)

    for it in range(1000):
        move = random.choice(list(MOVES.keys()))
        if not perform_move(field, move) is None:
            field = perform_move(field, move)

    return field


def print_field(field):
    """
    This function prints field to user.

    :param field: current field state to be printed.
    :return: None
    """
    print()
    print(*field[0:4])
    print(*field[4:8])
    print(*field[8:12])
    print(*field[12:16])
    print()


def is_game_finished(field):
    """
    This function checks if the game is finished.

    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    for x in range(15):
        if field[x] != x + 1:
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
    nfield = field.copy()
    move = MOVES[key]

    empty_pos = field.index(EMPTY_MARK)
    if move == 1 and empty_pos % 4 == 3:
        return None
    if move == -1 and empty_pos % 4 == 0:
        return None
    if move == 4 and empty_pos // 4 == 3:
        return None
    if move == -4 and empty_pos // 4 == 0:
        return None
        
    nfield[empty_pos],nfield[empty_pos + move] = nfield[empty_pos + move], nfield[empty_pos]
    return nfield


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
    while True:
        move = input(
     """
List of accepted moves:
    'w' - up,
    's' - down,
    'a' - left,
    'd' - right
Enter your move : """
        )
        try:
            MOVES[move]
            return move
        except KeyError:
            print("It is not move")


def main():
    """
    The main function. It starts when the program is called.

    It also calls other functions.
    :return: None
    """
    field = shuffle_field()
    while not is_game_finished(field):
        print_field(field)
        move = handle_user_input()
        if perform_move(field, move) is None:
            print("Move can't be done")
        else:
            field = perform_move(field, move)
    print("You win")
    print_field(field)


if __name__ == '__main__':
    main()
