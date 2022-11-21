from loguru import logger
import time
import csv
import httpx
from hw_7.write_data import write_data_xml

async def start_parsing():
    all_emails_not_flatten = parse_emails_from_csv_file()
    # Вытягиваю list of lists в простой list и преобразую его в dict
    emails_ids = dict.fromkeys(flatten(all_emails_not_flatten))
    logger.info('This program work with {number_users} users'.format(number_users = len(emails_ids)))
    people_data = await get_data_json()
    emails_ids = get_ready_dict_with_emails_and_ids(people_data, emails_ids)
    print(emails_ids)
    await write_data_xml(emails_ids)


def parse_emails_from_csv_file():
    emails = []
    start_time = time.monotonic()
    with open('hw_7/emails_file.csv') as csv_file:
        reader = csv.reader(csv_file)
        end_time = time.monotonic()
        logger.info('Request lasted {0} seconds'.format(end_time - start_time))
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
        logger.info('The request lasted {0} seconds'.format(end_time - start_time))
        return response.json()


def get_ready_dict_with_emails_and_ids(people_data, emails_ids):
    for person_data in people_data:
        if person_data['email'] in emails_ids:
            emails_ids[person_data.get('email')] = person_data['id']
    return emails_ids