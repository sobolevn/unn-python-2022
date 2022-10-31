import re

from loguru import logger
from parsing_json import get_email_id, get_user_info
from read_csv import read
from writer import write


def start(emails_path: str, json_path: str):
    """This method calls other methods to make the program work."""
    types_info = ['posts', 'albums', 'todos']
    _user_xml_write(emails_path, json_path, types_info)


def _user_xml_write(emails_path: str, json_path: str, types_info: list):
    emails_id = _get_emails_id(emails_path, json_path)
    for key in emails_id:
        user_info = get_user_info(json_path, str(emails_id.get(key)), types_info)  # noqa: E501
        path = '../files/users/{0}.xml'.format(str(emails_id.get(key)))
        user_id = str(emails_id.get(key))
        write(user_id, str(key), user_info, types_info, path)


def _get_emails_id(emails_path: str, json_path: str) -> dict:
    emails = read(str(emails_path))
    all_emails_id = get_email_id(str(json_path))
    emails_id = dict()
    for key in emails:
        if _is_email(key):
            user_id = all_emails_id.get(key)
            if user_id is None:
                logger.warning('{0} is missing from the website'.format(key))
            else:
                emails_id[key] = user_id
        else:
            logger.warning('{0} is not valid email address'.format(key))
    logger.info('{0} users were found on the website.'.format(len(emails_id)))
    return emails_id


def _is_email(email: str) -> bool:
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')  # noqa: E501
    return re.fullmatch(regex, email) is not None
