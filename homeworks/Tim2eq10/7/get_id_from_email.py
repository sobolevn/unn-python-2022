import load
from exceptions import GetIdError
from logger_time import logger_time


@logger_time('getting id from email')
def get_id(user_email):
    users = load.users_list()

    for user in users:
        if user['email'] == user_email:
            return user['id']
    raise GetIdError
