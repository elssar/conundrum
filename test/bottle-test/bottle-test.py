#!/usr/bin/env python

from bottle import Bottle, run, post, request, static_file, TEMPLATE_PATH, jinja2_template as template
from json import loads
from datetime import datetime
import conundrum
from sys import path

app= Bottle()

css_url= path[0]+'/static/style.css'
syntax_url= path[0]+'/static/native.css'
TEMPLATE_PATH.append('./templates')

@app.route('/')
def index():
    archive= conundrum.archive()
    return template('layout.html', css_url=css_url, syntax_url=syntax_url, date= datetime.now().strftime('%B %d, %Y'), post=archive)

@app.route('/<post>')
def show_post():
    blog= conundrum.blog(post)
    if blog:
        return template('layout.html', css_url=css_url, syntax_url=syntax_url, date= blog[1], post= blog[0])
    else:
        return template('layout.html', css_url=css_url, syntax_url=syntax_url, date= datetime.now().strftime('%B %d, %Y'), post= 'Post not found')

@app.route('/fetch', methods= ['POST'])
def fetch():
    data= loads(request.data)
    res= conundrum.fetch(data['id'], data['title'], 'elssar')
    return 'Done' if res else 'Not Done!'

@app.route('/update', methods= ['POST'])
def update():
    data= loads(request.data)
    res= conundrum.update(data['title'])
    return 'Done' if res else 'Not Done'

if __name__=='__main__':
    app.run()