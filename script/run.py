#!/usr/bin/python3
import json

f = open('./test.json')
list1 = json.load(f)

print(list1[0]["user_name"])

for user in list1:
    print(user)
