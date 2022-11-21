import asyncio
import csv
from xml.etree import ElementTree as Et  # noqa: S405

from loguru import logger


def read_data(filename):
    """
    Read csv file.

    Umail saved all strings from csv.
    """
    logger.debug('Open {0}'.format(filename))
    with open(filename) as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
        umail = []
        for row in datareader:
            for enty in row:
                umail.append(enty)
    logger.debug('Close {0}'.format(filename))
    return umail


async def all_save_user_data(userdata, users, urldir):
    """
    Save all users data.

    Use for each user method _save_user_data.
    """
    await asyncio.gather(
        *[
            _save_user_data(userdata[key], key, users[key], urldir)
            for key in users.keys()
        ],
        return_exceptions=True,
    )


async def _save_user_data(jsdata, uid, email, urldir):  # noqa: WPS210
    mainel = Et.Element('user')
    Et.SubElement(mainel, 'id').text = str(uid)
    Et.SubElement(mainel, 'email').text = str(email)

    datavars = ['posts', 'albums', 'todos']
    for index, _ in enumerate(jsdata):
        fse = Et.SubElement(mainel, datavars[index])
        for udata in jsdata[index]:
            se = Et.SubElement(fse, datavars[index][:-1])
            for key in udata.keys():
                if key != 'userId':
                    sse = Et.SubElement(se, key)
                    sse.text = str(udata[key]).replace('\n', '')
    await _save_in_file(mainel, uid, urldir)


async def _save_in_file(mainel, uid, urldir):
    tree = Et.ElementTree(mainel)
    Et.indent(tree)
    with open(
        '{0}/{1}.xml'.format(urldir, uid),
        'wb',
    ) as xml_file:
        tree.write(xml_file, encoding='utf-8', xml_declaration=True)
    logger.debug('User id: {0} Saved'.format(uid))
