#!/usr/bin/python
#
# Framework agnostic blog generator in Python

__author__= 'elssar <elssar@altrawcode.com>'
__license__= 'BSD License'
__version__= '0.1.0'

from markdown import markdown
from yaml import load, dump
from sys import path, argv
from datetime import datetime
from requests import get, post
from json import loads
from os import getcwd

base= getcwd()+'/posts/'

def fetch(id, name, user):
    gist= get('http://api.github.com/gists/', headers={'user-agent': 'conundrum-blog-engine'})
    if user!= content['user']['login'] or gist.status_code!=200:
        return False
    content= loads(gist)
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

def blog(name):
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
    opts= {'-p': 4, '-u': 3}
    keys= ['title', 'id']
    if args[0] not in opts:
        print 'Invalid options'
        return False
    if len(args)!=opts[args[0]]:
        print 'Invalid arguments'
        return False
    payload= {}
    for key, value in zip(keys, args[2:]):
        payload[key]= value
    req= post(args[1], data=payload, headers={'user-agent': 'conundrum-operator'})
    print req.status_code

if __name__=='__main__':
    operate(*argv[1:])