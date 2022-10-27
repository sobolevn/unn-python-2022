from typing import cast

import requests
from loguru import logger

from csv_request_xml.api_types import BINDINGS, USERS_API_URL, User, UserAttrs


def _only_keys(dictionary: dict, keys: list) -> dict:
    return {
        dict_value: dictionary[dict_value]
        for dict_value in dictionary
        if dict_value in keys
    }


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

    for attr_name in UserAttrs.__annotations__:
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
            _only_keys(attr, list(related_type.__annotations__.keys()))
            for attr in request.json()
        ]

    return cast(UserAttrs, out)
