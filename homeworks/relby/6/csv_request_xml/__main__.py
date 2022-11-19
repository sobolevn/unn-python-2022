import asyncio
from typing import Final

from loguru import logger

from csv_request_xml.api_types import Email, User
from csv_request_xml.reader import read_emails_from_csv
from csv_request_xml.requester import get_user_attributes, get_users
from csv_request_xml.saver import save_to_xml

EMAILS_FILEPATH: Final = 'emails.csv'


def _configure_logger():
    logger.add(lambda _: exit(1), level='ERROR')  # noqa: WPS421


async def handle_email(email: Email, users: list[User]):
    logger.info('Start working with `{0}`'.format(email))
    user = next(
        (user for user in users if user['email'] == email),
        None,
    )
    if user is not None:
        attrs = await get_user_attributes(user)
        save_to_xml(user, attrs)
    else:
        logger.warning(
            'User with this email `{0}` was not found'.format(email),
        )


async def async_main() -> None:
    _configure_logger()
    emails = read_emails_from_csv(EMAILS_FILEPATH)
    users = await get_users()

    await asyncio.gather(*[
        handle_email(email, users)
        for email in emails
    ])


def main() -> None:
    asyncio.run(async_main())


if __name__ == '__main__':
    main()
# noqa: WPS473 (I suppose it's a bug)
