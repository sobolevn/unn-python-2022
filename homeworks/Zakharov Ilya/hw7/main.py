import csv
import requests
import json
import xml.etree.ElementTree as ET
from loguru import logger
import datetime as dt
import os

@logger.catch
def openpars(link, filik):
    dtn = dt.datetime.now()
    res = requests.get(link)
    logger.info('lead time to {site} is {time}',site=link, time=dt.datetime.now() - dtn)
    mylist = []
    obj = json.loads(res.text)
    # Спросить у преподователя насчёт open
    with open(filik) as file:
        reader = csv.reader(file)
        for row in reader:
            for modul in obj:
                if row[0] == modul['email']:
                    mydatadict = {}
                    mydatadict['id'] = modul['id']
                    mydatadict['email'] = row[0]
                    mylist.append(mydatadict)
        logger.info('number of users {}', len(mylist))
    return mylist
@logger.catch
def parsingsite(link, Attribute, list):
    mylist = []
    dtn = dt.datetime.now()
    row = requests.get(link)
    logger.info('lead time to {site} is {time}',site=link, time=dt.datetime.now() - dtn)
    objlink = json.loads(row.text)
    for modul in objlink:
        for i in list:
            if i['id'] == modul['id']:
                logger.info('Starts parsing for {email} in {site}', email=i['email'], site=link)
                i[Attribute] = modul
                mylist.append(i)
    return mylist
@logger.catch
def genetratexml(fileName, dict):
    trunk = ET.Element('User')
    ET.SubElement(trunk, 'id').text = f"{dict['id']}"
    ET.SubElement(trunk, 'email').text = f"{dict['email']}"
    posts0 = ET.SubElement(trunk, 'posts')
    if 'posts' in dict:
        posts = ET.SubElement(posts0, 'post')
        dictposts = dict['posts']
        ET.SubElement(posts, 'id').text = f"{dictposts['id']}"
        ET.SubElement(posts, 'title').text = f"{dictposts['title']}"
        ET.SubElement(posts, 'body').text = f"{dictposts['body']}"
    else:
        posts0.text = ' '
    albums0 = ET.SubElement(trunk, 'albums')
    if 'albums' in dict:
        albums = ET.SubElement(albums0, 'album')
        dictalbums = dict['albums']
        ET.SubElement(albums, 'id').text = f"{dictalbums['id']}"
        ET.SubElement(albums, 'title').text = f"{dictalbums['title']}"
    else:
        albums0.text = ' '
    todos0 = ET.SubElement(trunk, 'todos')
    if 'todos' in dict:
        todos = ET.SubElement(todos0, 'todo')
        dicttodos = dict['todos']
        ET.SubElement(todos, 'id').text = f"{dicttodos['id']}"
        ET.SubElement(todos, 'title').text = f"{dicttodos['title']}"
        ET.SubElement(todos, 'completed').text = f"{dicttodos['completed']}"
    else:
        todos0.text = ' '
    tree = ET.ElementTree(trunk)
    with open(fileName, 'wb') as file:
        ET.indent(tree, space="\t", level=0)
        tree.write(file)
    os.replace(fileName, f"Users/{fileName}")



if __name__ == '__main__':
    myfistlist = openpars('https://jsonplaceholder.typicode.com/users/', 'data.csv')
    parsingsite('https://jsonplaceholder.typicode.com/users/1/posts', 'posts', myfistlist)
    parsingsite('https://jsonplaceholder.typicode.com/users/1/albums', 'albums', myfistlist)
    parsingsite('https://jsonplaceholder.typicode.com/users/1/todos', 'todos', myfistlist)
    if not os.path.isdir('users'):
        os.mkdir('users')
    for mydict in myfistlist:
        genetratexml(f"{mydict['id']}.xml", mydict)




