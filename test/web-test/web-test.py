#!/usr/bin/env python

from json import loads
import conundrum
from datetime import datetime
import web
from web.contrib.template import render_jinja

urls= (
    '/', 'index',
    '/(.)', 'show',
    '/fetch', 'fetch',
    '/update', 'update',
    )

render= render_jinja('templates', encoding= 'utf-8')

class index:
    def GET(self):
        archive= conundrum.archive()
        return render.layout(css_url= css, color_url= color, date= datetime.now().strftime('%B %d, %Y'), post=archive)

class show:
    def GET(self, name):
        blog= conundrum.blog(name)
        if blog:
            return render.layout(css_url=css, color_url=color, date=blog[1], post=blog[0])
        else:
            return render.layout(css_url= css, color_url= color, date= datetime.now().strftime('%B %d, %Y'), post='Post not found')

class fetch:
    def POST(self):
        data= loads(request.data)
        res= conundrum.fetch(data['id'], data['title'], 'elssar')
        return 'Done' if res else 'Not Done!'

class update:
    def POST(self):
        data= loads(request.data)
        res= conundrum.update(data['title'])
        return 'Done' if res else 'Not Done!'

app= web.application(urls, globals())

if __name__=='__main__':
    app.run()