import asyncio
import json

from downloadjson import req_get_data, req_get_user_todo
from loguru import logger


async def get_list_id(url, mails):
    """
    Read csv file.

    Umail saved all strings from csv.
    """
    ans = {}
    logger.debug('Start parse users emails')
    js = json.loads(await req_get_data(url))
    for udata in js:
        if udata['email'] in mails:
            mails.remove(udata['email'])
            ans[udata['id']] = udata['email']
    if not mails:
        logger.warning('Not exist mails {0}'.format(str(mails)))
    return ans


async def _load_user_todo(url, uid, mail):
    logger.debug('Starts parsing for {0}'.format(mail))
    return [json.loads(rg) for rg in await req_get_user_todo(url, uid)]


async def all_load_user_data(url, users):
    """
    Load all user todo.

    Todo as posts, albums, todos.
    """
    logger.info('Users to parse {0}'.format(users))
    dictionary = {}
    results_utodo = await asyncio.gather(
        *[_load_user_todo(url, key, users[key]) for key in users.keys()],
        return_exceptions=True,
    )
    for index, key in enumerate(users.keys()):
        dictionary[key] = results_utodo[index]
    return dictionary
