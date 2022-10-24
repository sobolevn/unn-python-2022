import requests

from logger_time import logger_time


@logger_time('getting list of users')
def users_list():
    user_info_path = 'https://jsonplaceholder.typicode.com/users/'
    resp = requests.get(user_info_path)
    return resp.json()


@logger_time('getting posts')
def posts(user_id):
    root_path = 'https://jsonplaceholder.typicode.com/users'
    resp = requests.get('{0}/{1}/posts'.format(
        root_path,
        user_id,
    ))
    return resp.json()


@logger_time('getting albums')
def albums(user_id):
    root_path = 'https://jsonplaceholder.typicode.com/users'
    resp = requests.get('{0}/{1}/albums'.format(
        root_path,
        user_id,
    ))
    return resp.json()


@logger_time('getting todos')
def todos(user_id):
    root_path = 'https://jsonplaceholder.typicode.com/users'
    resp = requests.get('{0}/{1}/todos'.format(
        root_path,
        user_id,
    ))
    return resp.json()
