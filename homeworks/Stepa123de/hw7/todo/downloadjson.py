import httpx
import asyncio
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
    udata = []
    q = asyncio.Queue()
    task_list = []
    for vardata in datavars:
        task = asyncio.create_task(req_get_data('{0}{1}{2}'.format(url, str(userid), vardata)))
        task_list.append(task)

    await q.join()
    await asyncio.gather(*task_list,return_exceptions=True)

    return list(i.result() for i in task_list)
