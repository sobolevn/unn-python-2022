from typing import Final

from loguru import logger

from inputdata import all_save_user_data, read_data
from workwithjson import all_load_user_data, get_list_id

CSVDATA: Final = '../files/email/data.csv'
MYDIR: Final = '../files/users'
URL: Final = 'https://jsonplaceholder.typicode.com/users/'



def main():
    """
    Main method.

    mails get strring from .csv file
    users get users in URL with mails
    alluserdata get todo of all users
    all_save_user_data save all user data in files
    """
    mails = read_data(CSVDATA)
    users = get_list_id(URL, mails)
    users_todo = all_load_user_data(URL, users)
    all_save_user_data(users_todo, users, MYDIR)


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        logger.critical(ex)
