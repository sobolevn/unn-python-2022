"""Functions for getting users data."""
import csv

from loguru import logger
from requests import get


def call_getter(attribute):
    """
    Call the users data getter.

    Args:
        attribute: getter key

    Returns:
        return getter for get users data
    """
    return data_getters[attribute]


def _get_general_data():
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = get(url)
    response.raise_for_status()
    return response.json()


def _get_users_id(emails):
    users_data = _get_general_data()
    users_id = []
    for email in emails:
        for this_user in users_data:
            if email == this_user['email']:
                users_id.append(this_user['id'])
                break

    if len(emails) != len(users_id):
        logger.warning(
            '{0} emails were not found'.format(len(emails) - len(users_id)),
        )

    return users_id


def _get_csv_emails(location):
    row_data = []
    with open(location) as file_emails:
        reader = csv.reader(file_emails, delimiter=';')
        for row in reader:
            row_data.extend(list(row))

    logger.info(
        'Number of users on checking the email: {0}'.format(len(row_data)),
    )
    return row_data


def _get_user_activity(user, activity=''):
    base_url = 'https://jsonplaceholder.typicode.com/users/'
    url = base_url + '{0}/{1}'.format(str(user), activity)
    response = get(url)
    response.raise_for_status()
    return response.json()


data_getters = {
    'general': _get_general_data,
    'id_from_email': _get_users_id,
    'csv_emails': _get_csv_emails,
    'activity': _get_user_activity,
}
