from typing import Final

from ToStart import start
from loguru import logger


def main():
    """The Main method - starting point of our program"""
    try:
        start(EMAILS_PATH, JSON_PATH)
    except Exception as ex:
        logger.exception("Something went wrong.", ex)


if __name__ == '__main__':
    EMAILS_PATH: Final = '../files/emails/email.csv'
    JSON_PATH: Final = 'https://jsonplaceholder.typicode.com/users/'
    try:
        main()
    except KeyboardInterrupt:
        logger.critical("Something went wrong.")
