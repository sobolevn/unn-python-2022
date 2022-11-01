"""Save users data into .xml files."""
from os import mkdir, path

from loguru import logger
from lxml import etree  # noqa: S410

from users_data import call_getter


def _add_attribute(user, active, attrs, user_node):
    node = etree.SubElement(user_node, '{0}s'.format(active))
    activities = call_getter('activity')(user, '{0}s'.format(active))

    for activity in activities:
        act_node = etree.SubElement(node, active)
        for attr in attrs:
            etree.SubElement(act_node, attr).text = str(activity[attr])


def _write_data(this_id, this_email):
    root = etree.Element('user')

    etree.SubElement(root, 'id').text = str(this_id)
    etree.SubElement(root, 'email').text = this_email

    base_attrs = ('id', 'title')

    _add_attribute(this_id, 'post', base_attrs + ('body', ), root)
    _add_attribute(this_id, 'album', base_attrs, root)
    _add_attribute(this_id, 'todo', base_attrs + ('completed', ), root)

    etree.ElementTree(root).write(
        'users/{0}/data.xml'.format(this_id),
        encoding='UTF-8',
        xml_declaration=True,
        pretty_print=True,
    )
    logger.success(
        'Data has been uploaded into users/{0}/data.xml'.format(this_id),
    )


def create_files(emails_file):
    """
    Create files for saving users data.

    Args:
        emails_file: location of the emails file
    """
    if not path.exists('users'):
        mkdir('users')
        logger.success('The folder "users" has been created')

    emails = call_getter('csv_emails')(emails_file)
    ids = call_getter('id_from_email')(emails)
    logger.info('Number of users for parsing: {0}'.format(len(ids)))

    for user_number, user_id in enumerate(ids):
        user_email = emails[user_number]
        logger.info('Starts parsing for {0}'.format(user_email))

        if not path.exists('users/{0}'.format(user_id)):
            mkdir('users/{0}'.format(user_id))

        _write_data(str(user_id), user_email)
