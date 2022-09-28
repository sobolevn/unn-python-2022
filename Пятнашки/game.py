
import random


EMPTY_MARK = 'x |'


MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():

    a = ['x |','1 |','2 |','3 |','4 |','5 |','6 |','7 |','8 |','9 |','10|','11|','12|','13|','14|','15|']
    random.shuffle(a)
    return a

     


def print_field(field):
    k = 0
    for i in field:
        k+=1
        print(i,end = '')
        if k%4 == 0:
            print(f"\n",end = '')



def is_game_finished(field):

    c = []
    if field[0] == EMPTY_MARK:
        return False
    for i in field:
        c.append(i)
    if c == sorted(field):
        return True
    return False


def perform_move(field, key):

    for i in range(16):
        if field[i] == EMPTY_MARK:
            f = i+MOVES[key]
            if f >15 or f<0:
                print('None')
                break
            t = field[f]
            field[i+MOVES[key]] = field[i]
            field[i] = t
            break


def handle_user_input():

    w = '123'
    while not(w in MOVES):
        w = input()
    return w


def main():
    Field = shuffle_field()
    while True:
        print_field(Field)
        Key = handle_user_input()
        perform_move(Field, Key)
        if is_game_finished(Field):
            break



if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    main()
