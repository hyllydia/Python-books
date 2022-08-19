#coding:utf-8
def remove_char(ind,str1):
    # l1=list(str1)
    # if l1[ind]:
    #     l1.remove(l1[ind])
    # new_str=''.join(l1)
    # return new_str
    return str1[:ind]+str1[ind+1:]

if __name__=="__main__":
    new_str=remove_char(2,'python！')
    print(new_str)