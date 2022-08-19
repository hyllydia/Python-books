#coding:utf-8
import json
filename='ARP'
new_filename='new_arp.json'
with open(filename,'r') as f:
    #将json文件转化为Python格式
    data=json.load(f)
print(data)
#casebody=[]
#caseobj={'arp_case':casebody}
data['arp']['entry'][1]['ip']='9.0.1.1'
data['arp']['entry'][1]['mac']='001100000011'
#json_data=json.dumps(data)
with open(new_filename,'w') as fp:
    fp.write(json.dumps(data,indent=2))
    #json.dump(data,fp,indent=4)

