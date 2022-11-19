import asyncio
from typing import cast

import httpx
from loguru import logger

from csv_request_xml.api_types import BINDINGS, USERS_API_URL, User, UserAttrs


def _only_keys(dictionary: dict, keys: list) -> dict:
    return {
        dict_value: dictionary[dict_value]
        for dict_value in dictionary
        if dict_value in keys
    }


async def get_users() -> list[User]:
    async with httpx.AsyncClient() as client:
        request = await client.get(USERS_API_URL)
        logger.info('Request to {0} took {1} '.format(
            USERS_API_URL,
            request.elapsed,
        ))
        return request.json()


async def get_user_attribute(
    user: User,
    attr_name: str,
    client: httpx.AsyncClient,
) -> list[dict]:
    related_type = BINDINGS[attr_name]
    api_route = '{0}/{1}/{2}'.format(
        USERS_API_URL,
        user['id'],
        attr_name,
    )
    response = await client.get(api_route)
    logger.info('Request to {0} took {1}'.format(
        api_route,
        response.elapsed,
    ))
    return [
        _only_keys(attr, list(related_type.__annotations__.keys()))
        for attr in response.json()
    ]


async def get_user_attributes(user: User) -> UserAttrs:  # noqa: WPS210
    out = {}
    async with httpx.AsyncClient() as client:
        attr_names = UserAttrs.__annotations__
        user_attributes = await asyncio.gather(*[
            get_user_attribute(user, attr_name, client)
            for attr_name in attr_names
        ])
        for attr_name, user_attribute in zip(attr_names, user_attributes):
            out[attr_name] = user_attribute

    return cast(UserAttrs, out)
