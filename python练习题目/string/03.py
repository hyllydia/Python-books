#coding:utf-8

def new_str(str):
    #标准答案
    if len(str)<2:
        return 'Empty string'
    return str[0:2]+str[-2:]
if __name__=="__main__":
    str_res1=new_str("w3resource")
    print(str_res1)
    str_res2=new_str("w3")
    print(str_res2)
    str_res3=new_str('w')
    print(str_res3)
