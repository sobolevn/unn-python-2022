import csv

from loguru import logger

from csv_request_xml.api_types import Email
from csv_request_xml.handlers import is_email


def read_emails_from_csv(filepath: str) -> list[Email]:
    emails: list[Email] = []
    with open(filepath, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            for entry in line:
                if is_email(entry):
                    emails.append(entry)
                else:
                    logger.warning(
                        '`{0}` is not valid email. Skipping it'.format(
                            entry,
                        ),
                    )
    logger.info('{0} users were read from csv file'.format(len(emails)))
    return emails
