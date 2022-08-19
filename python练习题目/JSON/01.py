#coding:utf-8
#Write a Python program to convert JSON data to Python object
# import json
# json_data='{ "Name":"David", "Class":"I", "Age":6 }'
# d=json.loads(json_data)
# #loads将json字符串，byte转化为python字典
# print(type(d))
# print(d)
# print('\n')
#
# d={'Name': 'David', 'Class': 'I', 'Age': 6,'address':'shanghai'}
# print(type(d))
# json_s=json.dumps(d)
# #dumps()将字典转化为json字符串
# print(type(json_s))
# print(json_s)

# !/usr/bin/python3

import json

# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)
print(type(json_str))
