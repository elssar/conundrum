#!/usr/bin/python

from distutils.core import setup

setup(name= 'conundrum',
    version= '0.1.0',
    author= 'elssar',
    author_email= 'elssar@altrawcode.com',
    py_modules= ['conundrum.py',],
    url= 'https://github.com/elssar/conundrum',
    licence= 'MIT',
    description= 'A framework agnostic blog generator.',
    long_description= open('README.md').read(),
    install_requires= [
        'PyYAML >= 3.10',
        'Markdown >= 2.2.0',
        'requests >= 1.0.4'
        ],
)
