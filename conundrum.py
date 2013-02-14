#!/usr/bin/env python

"""
conundrum - a web framework agnostic blogging plugin in Python

The idea is pretty simple. To make a new post -
  - Fetch a public gist* from github, with a markdown file
  - Save as markdown text in a yaml file with other info like date
  - Keep a file with the name of the newest post
  - Maintain an archive

And to display -
  - Archive is returned as html
  - Blog post is returned as html if name is given, else the newest post is returned

* - For now it is possible to fetch post only from public gists. Support for more services will be added later.
"""

__author__= 'elssar <elssar@altrawcode.com>'
__license__= 'MIT'
__version__= '0.1.0'

from markdown import markdown
from yaml import load, dump
from sys import path, argv
from datetime import datetime
from requests import get, post
from json import loads, dumps

base= path[0]+'/posts/'

def fetch(id, name, user):
    gist= get('https://api.github.com/gists/'+id, headers={'user-agent': 'conundrum-blog-framework'})
    content= loads(gist.content)
    if user!= content['user']['login'] or gist.status_code!=200:
        return False
    data= {'date': datetime.now().strftime('%B %d, %Y')}
    data['description']= content['description']
    for f in content['files']:
        if content['files'][f]['language']=='Markdown':
            data['post']= content['files'][f]['content']
            data['url']= content['files'][f]['raw_url']
            data['title']= content['files'][f]['filename']
            data['author']= content['user']['login']
    with open(base+name+'.yaml', 'w') as post:
        dump(data, post)
    with open(base+'first', 'w') as f:
        f.write(name+'.yaml')
    with open(base+'archive.md', 'a') as archive:
        line= ' - [{0}]({1})   ({2})\n'.format(data['title'], name, data['date'])
        archive.write(line)
    return True

def update(name):
    try:
        with open(base+name+'.yaml', 'r') as f:
            data= load(f)
    except IOError:
        return False
    post= get(data['url'], headers={'user-agent': 'conundrum-blog-engine'})
    if post.status_code!=200:
        return False
    data['post']= post.text
    with open(base+name+'.yaml', 'w') as f:
        dump(data, f)
    return True

def blog(name=None):
    try:
        if name is None:
            with open(base+'first', 'w') as f:
                name= f.read()
        with open(base+name+'.yaml', 'r') as f:
            data= load(f)
    except IOError:
        return False
    post= markdown(data['post'], ['codehilite'])
    return post, data['date']
    

def archive():
    try:
        with open(base+'archive.md', 'r') as f:
            data= f.readlines()
        arch= ''.join(data[::-1])
        return markdown(arch)
    except IOError:
        return False

def operate(*args):
    opts= ['-p' , '-u']
    keys= ['title', 'id', 'auth']
    headers= {'User-Agent': 'conundrum-operator', 'Content-Type': 'application/json'}
    if args[0] not in opts:
        print 'Invalid options'
        return False
    payload= {}
    for key, value in zip(keys, args[2:]):
        payload[key]= value
    body= dumps(payload)
    req= post(args[1], data= body, headers= headers)
    print req.status_code

if __name__=='__main__':
    operate(*argv[1:])
