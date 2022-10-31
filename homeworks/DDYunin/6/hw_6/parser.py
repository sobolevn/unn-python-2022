import csv
from datetime import datetime

import requests
from loguru import logger

from hw_6.write_data import write_data_xml

# TODO
# Добавить логи
# Раскидать содержимое модуля на разные модули, ибо слишком много и сложно!


def start_parsing():
    all_emails_not_flatten = parse_emails_from_csv_file()
    # Вытягиваю list of lists в простой list и преобразую его в dict
    emails_ids = dict.fromkeys(flatten(all_emails_not_flatten))
    logger.info('This program work with {0} users'.format(len(emails_ids)))
    people_data = get_data_json()
    emails_ids = get_ready_dict_with_emails_and_ids(people_data, emails_ids)
    write_data_xml(emails_ids)


def parse_emails_from_csv_file():
    emails = []
    start_time = datetime.now()
    with open('hw_6/emails_file.csv') as csv_file:
        reader = csv.reader(csv_file)
        end_time = datetime.now()
        logger.info('Request lasted {0} seconds'.format(end_time - start_time))
        emails = list(reader)
    return emails


def flatten(lst_emails):
    return [lst_element for sublist in lst_emails for lst_element in sublist]


def get_data_json():
    url = 'https://jsonplaceholder.typicode.com/users/'
    start_time = datetime.now()
    response = requests.get(url)
    end_time = datetime.now()
    logger.info('The request lasted {0} seconds'.format(end_time - start_time))
    return response.json()


def get_ready_dict_with_emails_and_ids(people_data, emails_ids):
    for person_data in people_data:
        if person_data['email'] in emails_ids:
            emails_ids[person_data.get('email')] = person_data['id']
    return emails_ids
