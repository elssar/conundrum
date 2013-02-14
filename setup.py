#!/usr/bin/env python

from setuptools import setup
import os

with open(os.path.join(os.path.dirname(__file__), 'README.md') as readme:
    ld= readme.read()

setup(name= 'conundrum',
    version= '0.1.0',
    author= 'elssar',
    author_email= 'elssar@altrawcode.com',
    py_modules= ['conundrum'],
    url= 'https://github.com/elssar/conundrum',
    license= 'MIT',
    description= 'A web framework agnostic blogging plugin.',
    long_description= ld,
    install_requires= [
        'PyYAML >= 3.0.9',
        'Markdown >= 2.2.0',
        'requests >= 1.0.4',
        ],
    keywords= 'conundrum blog blogging plugin',
)
