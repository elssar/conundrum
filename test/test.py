#!/usr/bin/env python

import conundrum
from sys import argv
from requests import post
from json import dumps

gists= ['4760090', '4760103', '4760320']

def stand_alone():
    for i, gist in enumerate(gists):
        print conundrum.fetch(gist, `i+1`, 'elssar')
    print conundrum.archive()
    for i in xrange(1, 4):
        blog= conundrum.blog(`i`)
        if blog:
            print blog[1]
            print blog[0]
        else:
            print blog
    print conundrum.update('1')

def test_local(port):
    url= 'http://localhost:{0}/fetch'.format(port)
    for i, gist in enumerate(gists):
        payload= dumps({'id': gist, 'title': `i`})
        res= post(url, data= payload)
        print res.content

if __name__=='__main__':
    if len(argv)==1:
        stand_alone()
    elif len(argv)==2 and argv[1].isdigit():
        test_local(argv[1])
    else:
        print 'Usage -\npython test.py <port>\n'
