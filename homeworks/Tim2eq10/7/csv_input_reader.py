import csv

from load import logger_time


@logger_time('getting email list')
def get_email_list(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(
            csv_file, delimiter=',',
        )
        return list(*reader)
