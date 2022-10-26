from typing import Final

from loguru import logger

from csv_request_xml.reader import read_emails_from_csv
from csv_request_xml.requester import get_user_attributes, get_users
from csv_request_xml.saver import save_to_xml

EMAILS_FILEPATH: Final = 'emails.csv'


def main() -> None:
    emails = read_emails_from_csv(EMAILS_FILEPATH)
    users = get_users()

    for email in emails:
        user = next(
            (user for user in users if user['email'] == email),
            None,
        )
        if user is not None:
            attrs = get_user_attributes(user)
            save_to_xml(user, attrs)
        else:
            logger.warning(
                'User with this email `{0}` was not found'.format(email),
            )


if __name__ == '__main__':
    main()
