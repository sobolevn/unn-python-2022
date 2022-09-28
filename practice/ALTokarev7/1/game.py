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

CONTROL_BUTTONS = ("w", "s","a","d")

TRUE_POS = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,"x")

def shuffle_field():

    shuffled_tiles = list(TRUE_POS)

    for move in range(100):
        perform_move(shuffled_tiles, random.choice(CONTROL_BUTTONS))

    return shuffled_tiles


def print_field(field):

    for i in range(4):
        print("|", field[i*4],"\t",
                   field[i*4 + 1],"\t",
                   field[i*4 + 2],"\t",
                   field[i*4 + 3],"\t","|")

    return


def is_game_finished(field):
    if tuple(field) == TRUE_POS:
        return True
    return False


def perform_move(field, key):

    empty_ind = field.index("x")

    new_ind = empty_ind + MOVES[key]
    if new_ind < 0 or new_ind > 15:
        return None
    
    field[empty_ind], field[new_ind] = field[new_ind], field[empty_ind]
    return field

def handle_user_input():

    move = input("choose you move: ")
    while move not in CONTROL_BUTTONS:
        print("Enter only : 'w', 's','a','d'") 
        move = input("choose you move: ")

    return move

def main():
    
    field = shuffle_field()
    while not is_game_finished(field):
        print_field(field)
        if perform_move(field, handle_user_input()) is None:
            print("Invalid move!!!")
            continue 
    
    print("You`re champion!!!")

if __name__ == '__main__':
    main()
