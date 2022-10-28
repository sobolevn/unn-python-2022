from lxml import etree  # noqa: S410

import load


def set_id_subelem(root, full_object):
    id_elem = etree.SubElement(root, 'id')
    id_elem.text = str(full_object['id'])


def set_title_subelem(root, full_object):
    title_elem = etree.SubElement(root, 'title')
    title_elem.text = full_object['title'].replace('\n', ' ')


def posts(user_posts):
    root = etree.Element('posts')
    for user_post in user_posts:
        sub = etree.SubElement(root, 'post')

        set_id_subelem(sub, user_post)
        set_title_subelem(sub, user_post)
        post_body = etree.SubElement(sub, 'body')
        post_body.text = user_post['body'].replace('\n', ' ')

    return root


def albums(user_albums):
    root = etree.Element('albums')
    for user_album in user_albums:
        sub = etree.SubElement(root, 'album')

        set_id_subelem(sub, user_album)
        set_title_subelem(sub, user_album)

    return root


def todos(user_todos):
    root = etree.Element('todos')
    for user_todo in user_todos:
        sub = etree.SubElement(root, 'todo')

        set_id_subelem(sub, user_todo)
        set_title_subelem(sub, user_todo)
        todo_completed = etree.SubElement(sub, 'completed')
        todo_completed.text = str(user_todo['completed'])

    return root


def user(user_id):
    root = etree.Element('user')

    root.append(posts(load.posts(user_id)))
    root.append(albums(load.albums(user_id)))
    root.append(todos(load.todos(user_id)))

    return root
