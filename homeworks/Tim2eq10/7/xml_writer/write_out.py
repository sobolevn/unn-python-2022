import os
import xml.dom.minidom as md
import xml.etree.ElementTree as Xml

import xml_writer.xml_element as xml_el


def pretty_xml(root):
    xmlstr = Xml.tostring(root).decode()
    newxml = md.parseString(xmlstr)
    return newxml.toprettyxml(indent='  ', newl='\n')


def info(user_id):
    xml_path = os.path.join(
        'users', '{0}'.format(user_id),
    )
    xml_name = 'info.xml'

    outxml = pretty_xml(xml_el.user(user_id))

    if not os.path.isdir(xml_path):
        os.makedirs(xml_path)
    outpath = os.path.join(xml_path, xml_name)

    with open(outpath, 'w') as tree_file:
        tree_file.write(outxml)
