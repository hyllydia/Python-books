"""
实现将字符串k1:v1|k2:v2|k3:v3处理成字典{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}。
"""
def change(str):
    l=str.split("|")
    d={}
    for item in l:
        m=item.split(":")
        d[m[0]]=m[1]
    return d
if __name__=="__main__":
    print(change('k1:v1|k2:v2|k3:v3'))