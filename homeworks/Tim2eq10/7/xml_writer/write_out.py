import os

from lxml import etree  # noqa: S410

from xml_writer import xml_element


def to_xml_file(user_id):
    xml_path = os.path.join(
        'users', '{0}'.format(user_id),
    )
    xml_name = 'info.xml'

    tree = xml_element.user(user_id)

    if not os.path.isdir(xml_path):
        os.makedirs(xml_path)
    outpath = os.path.join(xml_path, xml_name)

    with open(outpath, 'w') as tree_file:
        tree_file.write(etree.tostring(tree, pretty_print=True, encoding=str))
