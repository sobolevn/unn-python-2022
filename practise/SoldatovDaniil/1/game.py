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
    for i in range(1, 16):
        field.append(i)
    field.append(EMPTY_MARK)
    for i in range(100):
        random.shuffle(field)
    return field


def print_field(field):
    for i in range(0, 16):
        if field[i] == EMPTY_MARK or field[i] < 10:
            print(' ', end='')
        print(field[i], end=' | ')
        if i % 4 == 3:
            print()


def is_game_finished(field):
    for i in range(0, 15):
        if field[i] != i + 1:
            return False
    return True


def perform_move(field, key):
    for i in range(0, 16):
        if field[i] == EMPTY_MARK:
            emptyIndex = i

    if emptyIndex % 4 == 3 and key == "d":
        return None
    if emptyIndex % 4 == 0 and key == "a":
        return None
    if MOVES[key] + emptyIndex < 0 and 15 < MOVES[key] + emptyIndex:
        return None
    field[emptyIndex] = field[emptyIndex + MOVES[key]]
    field[emptyIndex + MOVES[key]] = EMPTY_MARK
    return field


def handle_user_input():
    userMove = input()
    if userMove not in ['w', 's', 'a', 'd']:
        return None
    return userMove


def main():
    myField = shuffle_field()

    while not(is_game_finished(myField)):
        print_field(myField)
        key = handle_user_input()
        perform_move(myField, key)


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    main()
