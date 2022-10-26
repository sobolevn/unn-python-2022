import requests
import xml.etree.ElementTree as ET
import os
import csv
import time
from loguru import logger


def parse_posts(user):
    user_posts = ET.SubElement(user, 'posts')
    person_posts_page = requests.get(f"https://jsonplaceholder.typicode.com/users/{person['id']}/posts")
    person_posts = person_posts_page.json()

    for post in person_posts:
        current_post = ET.SubElement(user_posts, 'post')
        current_post_id = ET.SubElement(current_post, 'id')
        current_post_id.text = str(post['id'])
        current_post_title = ET.SubElement(current_post, 'title')
        current_post_title.text = post['title']
        current_post_body = ET.SubElement(current_post, 'body')
        current_post_body.text = post['body']


def parse_albums(user):
    user_albums = ET.SubElement(user, 'albums')
    person_albums_page = requests.get(f"https://jsonplaceholder.typicode.com/users/{person['id']}/albums")
    person_albums = person_albums_page.json()

    for album in person_albums:
        current_album = ET.SubElement(user_albums, 'album')
        current_album_id = ET.SubElement(current_album, 'id')
        current_album_id.text = str(album['id'])
        current_album_title = ET.SubElement(current_album, 'title')
        current_album_title.text = album['title']


def parse_todos(user):
    user_todos = ET.SubElement(user, 'todos')
    person_todos_page = requests.get(f"https://jsonplaceholder.typicode.com/users/{person['id']}/todos")
    person_todos = person_todos_page.json()

    for todo in person_todos:
        current_todo = ET.SubElement(user_todos, 'todo')
        current_todo_id = ET.SubElement(current_todo, 'id')
        current_todo_id.text = str(todo['id'])
        current_todo_title = ET.SubElement(current_todo, 'title')
        current_todo_title.text = todo['title']
        current_todo_completed = ET.SubElement(current_todo, 'completed')
        current_todo_completed.text = str(todo['completed'])


logger.add("debug,log", format="{time} {message}", level="DEBUG")

if not os.path.exists("users"):
    os.mkdir("users")

page = requests.get('https://jsonplaceholder.typicode.com/users/')
data = page.json()

emails = set()
with open('emails.csv', 'r') as file:
    for address in (file.read()).split(sep=','):
        emails.add(address[1:-1])

logger.debug(f"{len(emails)} users to check")

for person in data:
    if person['email'] in emails:
        logger.debug(f"Starts parsing for {person['email']}")
        start_time = time.time()

        user = ET.Element('user')
        user_id = ET.SubElement(user, 'id')
        user_id.text = str(person['id'])
        user_email = ET.SubElement(user, 'email')
        user_email.text = person['email']

        parse_posts(user)
        parse_albums(user)
        parse_todos(user)

        ET.ElementTree(user).write(f'users/{person["id"]}')

        logger.debug(f"Time for parsing: {'%.2f' % (time.time() - start_time)}")