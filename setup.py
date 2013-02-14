#!/usr/bin/env python

from setuptools import setup
from sys import path

setup(name= 'conundrum',
    version= '0.1.0',
    author= 'elssar',
    author_email= 'elssar@altrawcode.com',
    py_modules= ['conundrum'],
    url= 'https://github.com/elssar/conundrum',
    license= 'MIT',
    description= 'A framework agnostic blog generator.',
    long_description= open(path[0]+'/README.md', 'r').read(),
    install_requires= [
        'PyYAML >= 3.0.9',
        'Markdown >= 2.2.0',
        'requests >= 1.0.4',
        ],
)
