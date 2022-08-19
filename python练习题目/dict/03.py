#coding:utf-8
# Write a Python script to concatenate following dictionaries to create a new one. Go to the editor
#
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
def connect_d(d1,d2,d3):
    d4={}
    for d in (d1,d2,d3):
        d4.update(d)
    return d4
if __name__=="__main__":
    dic1={1: 10, 2: 20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    dic_res=connect_d(dic1,dic2,dic3)
    print(dic_res)