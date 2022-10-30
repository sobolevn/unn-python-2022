"""Save users data into .xml files."""
from os import mkdir, path

from loguru import logger
from lxml import etree  # noqa: S410
from users_data import get_users_data


def _add_attribute(user, active, attrs, user_node):
    node = etree.SubElement(user_node, '{0}s'.format(active))
    activities = get_users_data('activity')(user, '{0}s'.format(active))
    for activity in activities:
        post_node = etree.SubElement(node, active)
        for attr in attrs:
            etree.SubElement(post_node, attr).text = str(activity[attr])


def _write_data(this_id, this_email):
    root = etree.Element('user')

    etree.SubElement(root, 'id').text = str(this_id)
    etree.SubElement(root, 'email').text = this_email

    base_attrs = ('id', )
    posts_attrs = ('title', 'body')
    albums_attrs = ('title', )
    todos_attrs = ('title', 'completed')

    _add_attribute(this_id, 'post', base_attrs + posts_attrs, root)
    _add_attribute(this_id, 'album', base_attrs + albums_attrs, root)
    _add_attribute(this_id, 'todo', base_attrs + todos_attrs, root)

    etree.ElementTree(root).write(
        'users/{0}/data.xml'.format(this_id),
        encoding='UTF-8',
        xml_declaration=True,
        pretty_print=True,
    )
    logger.success(
        'The data has been uploaded into users/{0}/data.xml'.format(this_id),
    )


def create_files():
    """Create files for saving users data."""
    if not path.exists('users'):
        mkdir('users')
        logger.success('The folder "users" has been created')

    for user_id in users:
        user_email = get_users_data('activity')(user_id)['email']
        logger.info('Starts parsing for {0}'.format(user_email))

        if not path.exists('users/{0}'.format(str(user_id))):
            mkdir('users/{0}'.format(str(user_id)))

        _write_data(str(user_id), user_email)


users = get_users_data('id')(get_users_data('csv_email'))
