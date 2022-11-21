import asyncio

import httpx
from loguru import logger

logstr = 'End parse Time: {0} Status: {1} Url: {2}'


async def req_get_data(url):
    """
    Get user data base.

    Return data from httpx get.
    """
    async with httpx.AsyncClient() as client:
        rg = await client.get(url)
        logger.debug(logstr.format(rg.elapsed, rg.status_code, url))
        return rg.text


async def req_get_user_todo(url, userid):  # noqa: D103
    """
    Get user data.

    Data as posts, albums, todos.
    """
    datavars = ['/posts', '/albums', '/todos']

    return await asyncio.gather(
        *[
            req_get_data('{0}{1}{2}'.format(url, str(userid), vardata))
            for vardata in datavars
        ],
        return_exceptions=True,
    )
