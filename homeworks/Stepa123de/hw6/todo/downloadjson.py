import requests
from loguru import logger

logstr = 'End parse Time: {0} Status: {1} Url: {2}'


def req_get_data(url):
    """
    Get user data base.

    Return data to search emails.
    """
    logger.debug('Start parse users emails')
    rg = requests.get(url)
    logger.debug(logstr.format(rg.elapsed, rg.status_code, url))
    return rg.text


def req_get_user_todo(url, userid):  # noqa: D103
    """
    Get user data.

    Data as posts, albums, todos.
    """
    datavars = ['/posts', '/albums', '/todos']
    udata = []
    for vardata in datavars:
        rg = requests.get('{0}{1}{2}'.format(url, str(userid), vardata))
        udata.append(rg.text)
        logger.debug(logstr.format(rg.elapsed, rg.status_code, url))
    return udata
