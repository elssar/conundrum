#!/usr/bin/python

from flask import Flask, url_for, render_template, redirect
import conundrum
from datetime import datetime
from json import loads

app= Flask(__name__)

@app.route('/')
def index():
    archive= conundrum.archive()
    return render_template('layout.html', date= datetime.now().strftime('%B %d, %Y'), post=archive)

@app.route('/<post>')
def show_post():
    blog= conundrum.blog(post)
    if blog:
        return render_template('layout.html', date= blog[1], post= blog[0])
    else:
        return render_template('layout.html', date= datetime.now().strftime('%B %d, %Y'), post= 'Post not found')

@app.route('/fetch', methods= ['POST'])
def fetch():
    data= loads(request.data)
    res= conundrum.fetch(data['id'], data['title'], 'elssar')
    return 'Done' if res else 'Not Done!'

@app.route('/update', methods= ['POST'])
def update():
    data= loads(request.data)
    res= conundrum.update(data['title'])
    return 'Done' if res else 'Not Done!'

if __name__=='__main__':
    app.run()