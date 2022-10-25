import json

from loguru import logger

from downloadjson import req_get_data, req_get_user_todo


def _create_json_users(url):
    js = req_get_data(url)
    return json.loads(js)


def get_list_id(url, mails):
    """
    Read csv file.

    Umail saved all strings from csv.
    """
    ans = {}
    for udata in _create_json_users(url):
        if udata['email'] in mails:
            mails.remove(udata['email'])
            ans[udata['id']] = udata['email']
    if not mails:
        logger.warning('Not exist mails {0}'.format(str(mails)))
    return ans


def _load_user_todo(url, uid, mail):
    logger.debug('Starts parsing for {0}'.format(mail))
    return [json.loads(rg) for rg in req_get_user_todo(url, uid)]


def all_load_user_data(url, users):
    """
    Load all user todo.

    Todo as posts, albums, todos.
    """
    logger.info('Users to parse {0}'.format(users))
    return {key: _load_user_todo(url, key, users[key]) for key in users.keys()}
