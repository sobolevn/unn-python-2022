from todo.custom_exceptions import UserExitException
from todo.runtime import parse_user_input, perform_command


def main():
    while True:
        try:
            perform_command(parse_user_input())
        except UserExitException:
            break
        except Exception as ex:
            print('You have done something wrong!', ex)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')
