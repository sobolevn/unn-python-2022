from datetime import datetime

from loguru import logger


def logger_time(name=''):
    def wrapper(func):
        def inner(*args):
            start_time = datetime.now()
            result = func(*args)
            end_time = datetime.now()

            logger.info('{0} | Duration: {1}s'.format(
                name,
                end_time - start_time,
            ))

            return result

        return inner

    return wrapper
