import xml.etree.ElementTree as Xml

import load


def post(user_post):
    root = Xml.Element('post')

    post_id = Xml.SubElement(root, 'id')
    post_id.text = str(user_post['id'])

    post_title = Xml.SubElement(root, 'title')
    post_title.text = user_post['title'].replace('\n', ' ')

    post_body = Xml.SubElement(root, 'body')
    post_body.text = user_post['body'].replace('\n', ' ')

    return root


def posts(user_posts):
    root = Xml.Element('posts')
    for user_post in user_posts:
        root.append(post(user_post))
    return root


def album(user_album):
    root = Xml.Element('album')

    album_id = Xml.SubElement(root, 'id')
    album_id.text = str(user_album['id'])

    album_title = Xml.SubElement(root, 'title')
    album_title.text = user_album['title'].replace('\n', ' ')

    return root


def albums(user_albums):
    root = Xml.Element('albums')
    for user_album in user_albums:
        root.append(album(user_album))
    return root


def todo(user_todo):
    root = Xml.Element('todo')

    todo_id = Xml.SubElement(root, 'id')
    todo_id.text = str(user_todo['id'])

    todo_title = Xml.SubElement(root, 'title')
    todo_title.text = user_todo['title'].replace('\n', ' ')

    todo_completed = Xml.SubElement(root, 'completed')
    todo_completed.text = str(user_todo['completed'])

    return root


def todos(user_todos):
    root = Xml.Element('todos')
    for user_todo in user_todos:
        root.append(todo(user_todo))
    return root


def user(user_id):
    root = Xml.Element('user')
    
    root.append(posts(load.posts(user_id)))
    root.append(albums(load.albums(user_id)))
    root.append(todos(load.todos(user_id)))

    return root
