import csv
import os
import re
import xml.etree.cElementTree as ET
from typing import Final, Literal, overload

import requests
from loguru import logger

from csv_request_xml.api_types import Album, Post, Todo, User  # type: ignore

EMAILS_FILEPATH: Final = 'emails.csv'
USERS_API_URL: Final = 'https://jsonplaceholder.typicode.com/users'


def is_email(entry: str) -> bool:
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    return re.match(regex, entry) is not None


def read_emails_from_csv(filepath: str) -> list[str]:
    emails: list[str] = []
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


@overload
def get_user_field_by_id(
    field: Literal['posts'],
    user_id: int,
) -> list[Post]: ...


@overload
def get_user_field_by_id(
    field: Literal['albums'],
    user_id: int,
) -> list[Album]: ...


@overload
def get_user_field_by_id(
    field: Literal['todos'],
    user_id: int,
) -> list[Todo]: ...


def get_user_field_by_id(
    field,
    user_id: int,
):
    api_route = '{0}/{1}/{2}'.format(
        USERS_API_URL,
        user_id,
        field,
    )
    request = requests.get(api_route)
    logger.info('Request to {0} took {1}'.format(
        api_route,
        request.elapsed
    ))
    return request.json()


def save_to_file(
    user: User,
    email: str,
    posts: list[Post],
    albums: list[Album],
    todos: list[Todo],
    filepath: str = 'users',
) -> None:
    os.makedirs(filepath, exist_ok=True)

    user_node = ET.Element('user')
    ET.SubElement(user_node, 'id').text = str(user['id'])
    ET.SubElement(user_node, 'email').text = email

    posts_node = ET.SubElement(user_node, 'posts')
    for post in posts:
        post_node = ET.SubElement(posts_node, 'post')
        ET.SubElement(post_node, 'id').text = str(post['id'])
        ET.SubElement(post_node, 'title').text = post['title']
        ET.SubElement(post_node, 'body').text = post['body']

    albums_node = ET.SubElement(user_node, 'albums')
    for album in albums:
        album_node = ET.SubElement(albums_node, 'album')
        ET.SubElement(album_node, 'id').text = str(album['id'])
        ET.SubElement(album_node, 'title').text = album['title']

    todos_node = ET.SubElement(user_node, 'todos')
    for todo in todos:
        todo_node = ET.SubElement(todos_node, 'todo')
        ET.SubElement(todo_node, 'id').text = str(todo['id'])
        ET.SubElement(todo_node, 'title').text = todo['title']
        ET.SubElement(todo_node, 'completed').text = str(todo['completed'])

    tree = ET.ElementTree(user_node)
    ET.indent(tree)
    tree.write('{0}/{1}.xml'.format(filepath, user['id']))
    logger.info('Saved {0}/{1}.xml for user with email `{2}`'.format(
        filepath,
        user['id'],
        user['email'],
    ))


def main() -> None:
    emails = read_emails_from_csv(EMAILS_FILEPATH)
    request = requests.get(USERS_API_URL)
    logger.info('Request to {0} took {1} '.format(
        USERS_API_URL,
        request.elapsed,
    ))
    users: list[User] = request.json()
    for email in emails:
        user = next(
            (user for user in users if user['email'] == email),
            None,
        )
        if user is not None:
            user_id = user['id']

            posts = get_user_field_by_id('posts', user_id)
            albums = get_user_field_by_id('albums', user_id)
            todos = get_user_field_by_id('todos', user_id)
            save_to_file(user, email, posts, albums, todos)
        else:
            logger.warning('User with this email `{0}` was not found'.format(email))


if __name__ == '__main__':
    main()
