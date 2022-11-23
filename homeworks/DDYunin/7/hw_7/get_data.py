import time

import httpx
from loguru import logger


async def get_user_data_posts(usr_id):
    async with httpx.AsyncClient() as client:
        url = 'https://jsonplaceholder.typicode.com/users/{0}/posts'.format(
            usr_id
            )
        start_time = time.monotonic()
        response = await client.get(url)
        end_time = time.monotonic()
        logger.info('The request lasted {0} seconds'.format(
            end_time - start_time)
                    )
        return response.json()


async def get_user_data_albums(usr_id):
    async with httpx.AsyncClient() as client:
        url = 'https://jsonplaceholder.typicode.com/users/{0}/albums'.format(
            usr_id
            )
        start_time = time.monotonic()
        response = await client.get(url)
        end_time = time.monotonic()
        logger.info('The request lasted {0} seconds'.format(
            end_time - start_time)
                    )
        return response.json()


async def get_user_data_todos(usr_id):
    async with httpx.AsyncClient() as client:
        url = 'https://jsonplaceholder.typicode.com/users/{0}/todos'.format(
            usr_id
            )
        start_time = time.monotonic()
        response = await client.get(url)
        end_time = time.monotonic()
        logger.info('The request lasted {0} seconds'.format(
            end_time - start_time)
                    )
        return response.json()
