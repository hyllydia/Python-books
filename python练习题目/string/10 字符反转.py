#coding:utf-8
#input:I am a #**student!##
#Expect output: student a am I
import re
def reverse_words(str1):
    regex=re.compile(r'.*?[A-Z].*?[a-z].*?]')
    mo=regex.search(str1)
    l1=mo.group()
    print(l1)
    l2=l1.split()
    new_str=' '.join(reversed(l2))
    return new_str
if __name__=="__main__":
    #str1=input("please input some words: ")
    str1='I am a #**student!##'
    str2=reverse_words(str1)
    print(str2)