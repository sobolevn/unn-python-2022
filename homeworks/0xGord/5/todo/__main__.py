"""
Main file. Contains program execution logic.
"""

import os
import sys

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)


from todo.custom_exceptions import UserExitException
from todo.runtime import parse_user_input, perform_command


def main():
    """
    Main method, works infinitely until user runs `exit` command.
    Or hits `Ctrl+C` in the console.
    """
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
