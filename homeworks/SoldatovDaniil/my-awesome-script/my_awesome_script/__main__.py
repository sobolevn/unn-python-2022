from cmdInput import cmd_input


def main():
    cmd_input()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Smthng wrng bb!')
