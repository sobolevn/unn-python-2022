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

    my_field = list()
    for i in range(1, 16):
        my_field.append(i)
    my_field.append(EMPTY_MARK)
    for move in range(100):
        random.shuffle(my_field)
    return my_field


def print_field(field):

    for i in range(len(field)):
        if field[i] == EMPTY_MARK or field[i] < 10:
            print(' ', end='')
        print(field[i], end=' | ')
        if i in [3, 7, 11]:
            print()
    print()


def is_game_finished(field):

    for i in range(len(field) - 1):
        if (i + 1) != field[i]:
            return False
    return True


def perform_move(field, key):
    emp_ind = 0
    for i in field:
        if i == EMPTY_MARK:
            emp_ind = field.index(i)
            break
    if emp_ind % 4 == 0 and key == 'a':
        return None
    if emp_ind % 4 == 3 and key == 'd':
        return None
    if emp_ind + MOVES[key] < 0:
        return None
    if emp_ind + MOVES[key] > 15:
        return None

    field[emp_ind], field[emp_ind + MOVES[key]] = field[emp_ind + MOVES[key]], field[emp_ind]
    return field

def handle_user_input():

    my_key = input()
    if my_key not in ['w', 'a', 's', 'd']:
        return None
    return my_key


def main():
    game_field = shuffle_field()
    while not is_game_finished(game_field):
        print_field(game_field)
        perform_move(game_field, handle_user_input())
    print("YOU WIN")


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    main()
