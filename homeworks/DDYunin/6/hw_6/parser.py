import csv
import requests
from loguru import logger
from datetime import datetime
from lxml import etree as et, objectify
import os
import shutil

# Можно ли возвращать значение прямо из контекстного менеджера, не будет ли это плохо?
# В файлах json в тексте содержатся спец симовл \n, в следствии чего текст переносится на новые строки, это надо исправлять или нет?

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
    with open('hw_6/emails_file.csv') as f:
        reader = csv.reader(f)
        end_time = datetime.now()
        logger.info('The request lasted {0} seconds'.format(end_time - start_time))
        emails = list(reader)
    return emails

def flatten(list_of_emails):
    return [item for sublist in list_of_emails for item in sublist]

def get_data_json():
    url = 'https://jsonplaceholder.typicode.com/users/'
    start_time = datetime.now()
    response = requests.get(url)
    end_time = datetime.now()
    logger.info('The request lasted {0} seconds'.format(end_time - start_time))
    return response.json()

def get_ready_dict_with_emails_and_ids(people_data, emails_ids):
    for item in people_data:
        if item['email'] in emails_ids:
            emails_ids[item['email']] = item["id"]
    return emails_ids

def write_data_xml(dict_emails_and_ids):
    create_catalog_users()
    for email in dict_emails_and_ids:
        logger.info('Starts parsing for {0}'.format(email))
        xml_struct = create_struct_xml_file(email, dict_emails_and_ids)
        xml_struct = add_posts_in_xml_file(xml_struct, email, dict_emails_and_ids)
        xml_struct = add_albums_in_xml_file(xml_struct, email, dict_emails_and_ids)
        xml_struct = add_todos_in_xml_file(xml_struct, email, dict_emails_and_ids)
        save_ready_xml_file(xml_struct, email, dict_emails_and_ids)

def create_struct_xml_file(user_email, all_data):
    struct = et.Element('user')
    id_element = et.SubElement(struct, 'id')
    id_element.text = '{0}'.format(all_data[user_email])
    email_element = et.SubElement(struct, 'email')
    email_element.text = '{0}'.format(user_email)
    return struct

def add_posts_in_xml_file(xml_struct, user_email, all_data):
    data_posts = get_user_data_posts(all_data[user_email])        
    posts_element = et.SubElement(xml_struct, 'posts')
    if not data_posts:
        posts_element.text = ''
    for post in data_posts:
        post_element = et.SubElement(posts_element, 'post')
        et.SubElement(post_element, 'id').text = '{0}'.format(post['id'])
        et.SubElement(post_element, 'title').text = '{0}'.format(post['title'])
        et.SubElement(post_element, 'body').text = '{0}'.format(post['body']).replace('\n', ' ')
    return xml_struct

def add_albums_in_xml_file(xml_struct, user_email, all_data):
    data_albums = get_user_data_albums(all_data[user_email])
    albums_element = et.SubElement(xml_struct, 'albums')
    if not data_albums:
        albums_element.text = ''
    for album in data_albums:
        album_element = et.SubElement(albums_element, 'album')
        et.SubElement(album_element, 'id').text = '{0}'.format(album['id'])
        et.SubElement(album_element, 'title').text = '{0}'.format(album['title'])
    return xml_struct

def add_todos_in_xml_file(xml_struct, user_email, all_data):
    data_todos = get_user_data_todos(all_data[user_email])
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
    start_time = datetime.now()
    with open('hw_6/users/{0}.xml'.format(all_data[user_email]), 'wb') as file:
        xml_file.write(file, encoding="UTF-8", pretty_print=True, xml_declaration = True)
        end_time = datetime.now()
        logger.info('The request lasted {0} seconds'.format(end_time - start_time))

def create_catalog_users():
    if os.path.exists("hw_6/users"):
        shutil.rmtree("hw_6/users")
    os.mkdir("hw_6/users")

def get_user_data_posts(user_id):
    url = 'https://jsonplaceholder.typicode.com/users/{0}/posts'.format(user_id)
    start_time = datetime.now()
    response = requests.get(url)
    end_time = datetime.now()
    logger.info('The request lasted {0} seconds'.format(end_time - start_time))
    return response.json()

def get_user_data_albums(user_id):
    url = 'https://jsonplaceholder.typicode.com/users/{0}/albums'.format(user_id)
    start_time = datetime.now()
    response = requests.get(url)
    end_time = datetime.now()
    logger.info('The request lasted {0} seconds'.format(end_time - start_time))
    return response.json()

def get_user_data_todos(user_id):
    url = 'https://jsonplaceholder.typicode.com/users/{0}/todos'.format(user_id)
    start_time = datetime.now()
    response = requests.get(url)
    end_time = datetime.now()
    logger.info('The request lasted {0} seconds'.format(end_time - start_time))
    return response.json()
