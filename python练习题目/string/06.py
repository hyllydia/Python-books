#coding:utf-8
def add_ing(str1):
    if len(str1)>2:
        if str1[-3:]=='ing':
            str1+='ly'
        else:
            str1+='ing'
    return str1

if __name__=="__main__":
    str_res1=add_ing('abc')
    print(str_res1)
    str_res2=add_ing('string')
    print(str_res2)
    str_res3=add_ing('xy')
    print(str_res3)