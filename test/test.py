#!/usr/bin/env python

import conundrum

gists= ['4760090', '4760103', '4760320']

for i, gist in enumerate(gists):
    print conundrum.fetch(gist, i, 'elssar')

print conundrum.archive()

for i in xrange(1, 4):
    blog= conundrum.blog(`i`)
    print blog[1]
    print blog[0]

print conundrum.update('1')