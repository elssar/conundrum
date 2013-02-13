#!/usr/bin/env python

import conundrum
from sys import args
from requests import post
from json import dumps

gists= ['4760090', '4760103', '4760320']

def stand_alone():
    for i, gist in enumerate(gists):
        print conundrum.fetch(gist, `i`, 'elssar')
    print conundrum.archive()
    for i in xrange(1, 4):
        blog= conundrum.blog(`i`)
        print blog[1]
        print blog[0]
    print conundrum.update('1')

def test_local(port):
    url= 'http://localhost:{0}/fetch'.format(port)
    for i, gist in enumerate(gists):
        payload= dumps({'id': gist, 'title': `i`})
        res= post(url, data= payload)
        print res.content

if __name__=='__main__':
    if len(args)==1:
        stand_alone()
    elif len(args)==2 and args[1].isdigit():
        test_local(args[1])
    else:
        print 'Usage -\npython test.py <port>\n'
