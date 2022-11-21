# Сначала напишу реализацию в один файл
import aiohttp
import asyncio
import time
import httpx
import csv
from loguru import logger
import os
import shutil
import xml.etree.ElementTree as et

def parse_csv_file(): # Не надо делать асинхронные вызовы
    emails = []
    start_time = time.monotonic()
    with open('hw_7/emails_file.csv') as csv_file:
        reader = csv.reader(csv_file)
        logger.info('Request lasted {0} seconds'.format(time.monotonic() - start_time))
        emails = list(reader)
    return emails

def flatten(lst_emails): #  не надо делать асинхронные вызовы
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

##########################################################

def create_catalog_users():
    if os.path.exists('hw_7/users'):
        shutil.rmtree('hw_7/users')
    os.mkdir('hw_7/users')

def create_struct_xml_file(user_email, all_data):
    struct = et.Element('user')
    id_element = et.SubElement(struct, 'id')
    id_element.text = '{0}'.format(all_data[user_email])
    email_element = et.SubElement(struct, 'email')
    email_element.text = '{0}'.format(user_email)
    return struct

async def add_posts_in_xml_file(xml_struct, user_email, all_data):
    data_posts = await get_user_data_posts(all_data[user_email])
    posts_element = et.SubElement(xml_struct, 'posts')
    if not data_posts:
        posts_element.text = ''
    for post in data_posts:
        post_element = et.SubElement(posts_element, 'post')
        et.SubElement(post_element, 'id').text = '{0}'.format(post['id'])
        et.SubElement(post_element, 'title').text = '{0}'.format(post['title'])
        str_body = '{0}'.format(post['body'])
        et.SubElement(post_element, 'body').text = str_body.replace('\n', ' ')
    return xml_struct

async def get_user_data_posts(usr_id):
    async with httpx.AsyncClient() as client:
        url = 'https://jsonplaceholder.typicode.com/users/{0}/posts'.format(usr_id)
        start_time = time.monotonic()
        response = await client.get(url)
        end_time = time.monotonic()
        logger.info('The request lasted {0} seconds'.format(end_time - start_time))
        return response.json()

async def get_user_data_albums(usr_id):
    async with httpx.AsyncClient() as client:
        url = 'https://jsonplaceholder.typicode.com/users/{0}/albums'.format(usr_id)
        start_time = time.monotonic()
        response = await client.get(url)
        end_time = time.monotonic()
        logger.info('The request lasted {0} seconds'.format(end_time - start_time))
        return response.json()


async def get_user_data_todos(usr_id):
    async with httpx.AsyncClient() as client:
        url = 'https://jsonplaceholder.typicode.com/users/{0}/todos'.format(usr_id)
        start_time = time.monotonic()
        response = await client.get(url)
        end_time = time.monotonic()
        logger.info('The request lasted {0} seconds'.format(end_time - start_time))
        return response.json()

async def add_albums_in_xml_file(xml_struct, user_email, all_data):
    data_albums = await get_user_data_albums(all_data[user_email])
    albums_element = et.SubElement(xml_struct, 'albums')
    if not data_albums:
        albums_element.text = ''
    for album in data_albums:
        album_element = et.SubElement(albums_element, 'album')
        et.SubElement(album_element, 'id').text = '{0}'.format(album['id'])
        et.SubElement(album_element, 'title').text = '{0}'.format(album['title'])
    return xml_struct


async def add_todos_in_xml_file(xml_struct, user_email, all_data):
    data_todos = await get_user_data_todos(all_data[user_email])
    todos_element = et.SubElement(xml_struct, 'todos')
    if not data_todos:
        todos_element.text = ''
    for todo in data_todos:
        todo_element = et.SubElement(todos_element, 'todo')
        et.SubElement(todo_element, 'id').text = '{0}'.format(todo['id'])
        et.SubElement(todo_element, 'title').text = '{0}'.format(todo['title'])
        et.SubElement(todo_element, 'completed').text = '{0}'.format(todo['completed'])
    return xml_struct


def save_ready_xml_file(xml_struct, user_email, all_data):
    xml_file = et.ElementTree(xml_struct)
    et.indent(xml_file)
    start_time = time.monotonic()
    with open('hw_7/users/{0}.xml'.format(all_data[user_email]), 'wb') as xml_fl:
        xml_file.write(xml_fl, encoding='UTF-8', short_empty_elements=False, xml_declaration=True)
        end_time = time.monotonic()
        logger.info('The request lasted {0} seconds'.format(end_time - start_time))

async def user_operation_async(email, all_data):
    print('Operation for {email}'.format(email=email))
    logger.info('Starts parsing for {0}'.format(email))
    xml_struct = create_struct_xml_file(email, all_data)
    xml_struct = await add_posts_in_xml_file(xml_struct, email, all_data)
    xml_struct = await add_albums_in_xml_file(xml_struct, email, all_data)
    xml_struct = await add_todos_in_xml_file(xml_struct, email, all_data)
    save_ready_xml_file(xml_struct, email, all_data)
    print('Operation ends for {email}'.format(email=email))

async def write_data_xml(emails_and_ids): # А вот тут уже нужна асинхронность
    # у меня есть список эмейлов и для каждого пользователя хорошо было бы делать всё асинхронно
    create_catalog_users()
    await asyncio.gather(*[
        user_operation_async(email, emails_and_ids)
        for email in emails_and_ids
    ])

##################################################

async def main():
    emails = parse_csv_file()
    emails = dict.fromkeys(flatten(emails))
    logger.info('This program work with {number_users} users'.format(number_users = len(emails)))
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