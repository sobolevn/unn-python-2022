import asyncio
import time

from loguru import logger

from hw_7.parser import (flatten, get_data_json,
                         get_ready_dict_with_emails_and_ids, parse_csv_file)
from hw_7.write_data import write_data_xml


async def main():
    emails = parse_csv_file()
    emails = dict.fromkeys(flatten(emails))
    logger.info('This program work with {number_users} users'.format(
        number_users=len(emails))
                )
    people_data = await get_data_json()
    emails = get_ready_dict_with_emails_and_ids(people_data, emails)
    print(emails)
    await write_data_xml(emails)

if __name__ == '__main__':
    start = time.monotonic()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
    loop.close()
    print('It took', time.monotonic() - start)
