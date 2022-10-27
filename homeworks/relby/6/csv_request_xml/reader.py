import csv
import os
import re

from loguru import logger

from csv_request_xml.api_types import Email


def _is_email(entry: str) -> bool:
    regex = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',
    )
    return re.match(regex, entry) is not None


def read_emails_from_csv(filepath: str) -> list[Email]:
    if not os.path.exists(filepath):
        logger.error('csv file with filepath `{0}` was not found'.format(
            filepath,
        ))

    logger.info('Start reading {0}'.format(filepath))
    emails: list[Email] = []
    with open(filepath, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            for entry in line:
                if _is_email(entry):
                    emails.append(entry)
                else:
                    logger.warning(
                        '`{0}` is not valid email. Skipping it.'.format(
                            entry,
                        ),
                    )
    if emails:
        logger.success('{0} emails were read from csv file.'.format(
            len(emails),
        ))
    else:
        logger.error('No valid username emails were found in {0}.'.format(
            filepath,
        ))
    return emails
