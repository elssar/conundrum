#!/usr/bin/python

from flask import Flask, url_for, render_template, redirect
import conundrum
from datetime import datetime

app= Flask(__name__)

gists= ['4760090', '4760103', '4760320']

@app.route('/')
def index():
    archive= conundrum.archive()
    render_template('layout.html', date= datetime.now().strftime('%B %d, %Y'), post=archive)

@app.route('/<post>')
def show_post():
    if post is None:
        redirect(url_for('index'))
    blog= conundrum.blog(post)
    if blog:
        render_template('layout.html', date= blog[1], post= blog[0])
    else:
        render_template('layout.html', date= datetime.now().strftime('%B %d, %Y'), post= 'Post not found')

@app.route('/fetch', methods= ['POST'])
def fetch():
    res= conundrum.fetch(request.headers['data']['id'], request.headers['data']['title'], 'elssar')
    return res

@app.route('/update', methods= ['POST'])
def update():
    res= conundrum.update(request.headers['data']['title'])
    return res

if __name__=='__main__':
    app.run()