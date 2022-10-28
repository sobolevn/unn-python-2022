from loguru import logger

from csv_input_reader import get_email_list
from get_id_from_email import get_id
from xml_writer import write_out


def parse(input_path):
    email_list = get_email_list(input_path)
    logger.info('Starts parsing for {0} users'.format(len(email_list)))
    for email in email_list:
        logger.info('Starts parsing for {0}'.format(email))
        try:
            user_id = get_id(email)
        except ValueError:
            logger.error('FAILED Invalid email, cant get id')
            continue
        except Exception as ex:
            logger.error('FAILED Cant get id {0}'.format(ex))
            continue

        write_out.to_xml_file(user_id)


if __name__ == '__main__':
    path = 'input.csv'
    parse(path)
