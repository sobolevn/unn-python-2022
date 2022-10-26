import os

from loguru import logger
from lxml import etree  # noqa: S410

from csv_request_xml.api_types import User, UserAttrs


def save_to_xml(
    user: User,
    attrs: UserAttrs,
    filepath: str = 'users',
) -> None:
    os.makedirs(filepath, exist_ok=True)

    user_id = user['id']

    user_node = etree.Element('user')

    etree.SubElement(user_node, 'id').text = str(user_id)
    etree.SubElement(user_node, 'email').text = user['email']

    _add_attr_to_xml(attrs, user_node)

    tree = etree.ElementTree(user_node)
    tree.write('{0}/{1}.xml'.format(filepath, user_id), pretty_print=True)
    logger.info('Saved {0}/{1}.xml for user with email `{2}`'.format(
        filepath,
        user_id,
        user['email'],
    ))


def _add_attr_to_xml(attrs, node) -> None:
    for attr, fields in attrs.items():
        attr_node = etree.SubElement(node, attr)
        _handle_fields(fields, attr_node, attr)


def _handle_fields(fields, attr_node, attr) -> None:
    for field in fields:  # type: ignore
        field_node = etree.SubElement(attr_node, attr[:-1])
        for field_name, field_value in field.items():
            etree.SubElement(
                field_node,
                field_name,
            ).text = str(field_value)
