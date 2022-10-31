import requests
from loguru import logger


def get_user_info(path: str, user_id: str, info_types: list) -> dict:
    """Receives the user information
    ('posts', 'albums', 'todos')
     by the id from the website."""
    user_info: dict[str:list] = {}
    logger.info('Parsing for ID: {0} : Start.'.format(user_id))
    for info_type in info_types:
        response = requests.get(path + '{0}/{1}'.format(user_id, info_type))
        user_info[info_type] = response.json()
        logger.info('Request for ID {0} to get {1} took {2}'.format(
            user_id,
            info_types,
            response.elapsed,
        ))
    logger.info('Parsing for ID: {0} : Finish.'.format(user_id))
    return user_info


def get_email_id(path: str) -> dict:
    """Receives the user ID by the email from the website."""
    user_email_id: dict[str:int] = {}
    user = 1
    logger.info('Requests from the website: Begin.')
    while True:
        response = requests.get(path + '/{0}'.format(user))
        user_info = response.json()
        if not user_info:
            break
        user_email_id[user_info.get('email')] = user_info.get('id')
        user += 1
    logger.info('Requests from the website: Finish.')

    return user_email_id
