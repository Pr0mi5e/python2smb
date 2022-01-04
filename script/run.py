#!/usr/bin/python3
import execjs
f = open('./sign.js', 'r', encoding='utf-8')
line = f.readline()
htmlstr = ''
while line:
    htmlstr = htmlstr + line
    line = f.readline()
# print(htmlstr)
ctx = execjs.compile(htmlstr)
params = {
    "appKey": "00000001",
    "format": "json",
    "v": "1.0",
    "timestamp": 1641284391.943,
    "service": "volcano.volbeacon.circle.course.list",
    "circleId": "2b72cc72-15ba-40dd-aedf-e8fa6e5dad7d",
    "onlineState": 3,
    "pageNo": 1,
    "pageSize": 10,
    "userId": "c0624c1b-45ac-41fe-85a7-354950782285",
    "tenantCode": "jji",
    "ns": ""
}
res = ctx.call('createSign', params)
print(res)