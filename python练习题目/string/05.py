#coding:utf-8
def change_char(str1,str2):
    new_str1=str2[0:2]+str1[2:]
    new_str2=str1[0:2]+str2[2:]
    new_str = new_str1+' '+new_str2
    return new_str
if __name__=="__main__":
    str_res=change_char('abc','xyz')
    print(str_res)
