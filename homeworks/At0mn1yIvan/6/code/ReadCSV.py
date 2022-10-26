import csv
from loguru import logger


def read(path: str = None) -> tuple:
    """Read the csv file."""
    with open(path) as file:
        emails: list[str] = []
        reader = csv.reader(file, delimiter=',', quotechar='"')
        for line in reader:
            emails.extend(line)
        logger.info('{0} users were read from csv file'.format(len(emails)))

    return tuple(emails)
