from datetime import datetime

import requests
from loguru import logger


def get_user_data_posts(usr_id):
    url = 'https://jsonplaceholder.typicode.com/users/{0}/posts'.format(usr_id)
    start_time = datetime.now()
    response = requests.get(url)
    end_time = datetime.now()
    logger.info('The request lasted {0} seconds'.format(end_time - start_time))
    return response.json()


def get_user_data_albums(usr_id):
    url = 'https://jsonplaceholder.typicode.com/users/{0}/albums'.format(usr_id)
    start_time = datetime.now()
    response = requests.get(url)
    end_time = datetime.now()
    logger.info('The request lasted {0} seconds'.format(end_time - start_time))
    return response.json()


def get_user_data_todos(usr_id):
    url = 'https://jsonplaceholder.typicode.com/users/{0}/todos'.format(usr_id)
    start_time = datetime.now()
    response = requests.get(url)
    end_time = datetime.now()
    logger.info('The request lasted {0} seconds'.format(end_time - start_time))
    return response.json()
