#coding:utf-8
import json
with open('old','r') as fb:
    data=json.load(fb)
    print(data)
    print(type(data))
with open('new_file','w') as f:
    json.dump(data,f,indent=4,sort_keys=True)
    