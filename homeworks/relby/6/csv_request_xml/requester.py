from typing import cast

import requests
from loguru import logger

from csv_request_xml.api_types import (
    BINDINGS,
    USER_ATTR_NAMES,
    USERS_API_URL,
    User,
    UserAttrs,
)
from csv_request_xml.handlers import only


def get_users() -> list[User]:
    request = requests.get(USERS_API_URL)
    logger.info('Request to {0} took {1} '.format(
        USERS_API_URL,
        request.elapsed,
    ))
    return request.json()


def get_user_attributes(
    user: User,
) -> UserAttrs:
    out = {}

    for attr_name in USER_ATTR_NAMES:
        related_type = BINDINGS[attr_name]
        api_route = '{0}/{1}/{2}'.format(
            USERS_API_URL,
            user['id'],
            attr_name,
        )
        request = requests.get(api_route)
        logger.info('Request to {0} took {1}'.format(
            api_route,
            request.elapsed,
        ))

        out[attr_name] = [
            only(attr, list(related_type.__annotations__.keys()))
            for attr in request.json()
        ]

    return cast(UserAttrs, out)
