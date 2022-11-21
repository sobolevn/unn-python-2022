import asyncio
from pathlib import Path
from typing import Final

from inputdata import all_save_user_data, read_data
from loguru import logger
from workwithjson import all_load_user_data, get_list_id

PRDIR: Final = Path.cwd()
CSVDATA: Final = PRDIR / 'files/email/data.csv'
MYDIR: Final = PRDIR / 'files/users'
URL: Final = 'https://jsonplaceholder.typicode.com/users/'


async def main():
    """
    Main method.

    mails get strring from .csv file
    users get users in URL with mails
    alluserdata get todo of all users
    all_save_user_data save all user data in files
    """
    mails = read_data(CSVDATA)
    users = await get_list_id(URL, mails)

    users_todo = await all_load_user_data(URL, users)
    await all_save_user_data(users_todo, users, MYDIR)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as ex:
        logger.critical(ex)
