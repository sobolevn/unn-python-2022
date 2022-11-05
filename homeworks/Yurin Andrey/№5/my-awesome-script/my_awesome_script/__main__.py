from .cmdInput import cmd_input


def main():
    try:
        cmd_input()
    except Exception as ex:
        print('You have done something wrong!', ex)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')

