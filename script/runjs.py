#!/usr/bin/python3
import execjs
f = open('./sign.js', 'r', encoding='utf-8')
line = f.readline()
htmlstr = ''
while line:
    htmlstr = htmlstr + line
    line = f.readline()
ctx = execjs.compile(htmlstr)

# 调用js方法
def run_js(params):
    return ctx.call('createSign', params)
