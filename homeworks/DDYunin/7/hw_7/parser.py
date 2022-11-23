import csv
import time

import httpx
from loguru import logger


def parse_csv_file():
    emails = []
    start_time = time.monotonic()
    with open('hw_7/emails_file.csv') as csv_file:
        reader = csv.reader(csv_file)
        logger.info('Request lasted {0} seconds'.format(
            time.monotonic() - start_time)
                    )
        emails = list(reader)
    return emails


def flatten(lst_emails):
    return [lst_element for sublist in lst_emails for lst_element in sublist]


async def get_data_json():
    async with httpx.AsyncClient() as client:
        url = 'https://jsonplaceholder.typicode.com/users/'
        start_time = time.monotonic()
        response = await client.get(url)
        end_time = time.monotonic()
        logger.info('The request lasted {0} seconds'.format(
            end_time - start_time)
                    )
        return response.json()


def get_ready_dict_with_emails_and_ids(people_data, emails_ids):
    for person_data in people_data:
        if person_data['email'] in emails_ids:
            emails_ids[person_data.get('email')] = person_data['id']
    return emails_ids
