#coding:utf-8
import re
def char_match(string):
    #patten=re.compile(r'ab*')
    patten = re.compile(r'ab+')
    #patten = re.compile(r'ab?')
    #patten = re.compile(r'ab{3}')
    #patten = re.compile(r'ab{2,3}')
    string=patten.search(string)
    return bool(string)
if __name__=="__main__":
    print(char_match("ac"))
    print(char_match('abc'))
    print(char_match('abbc'))
    print(char_match('abbbc'))
    print(char_match('cbab'))

    #serch()与match()的区别， match()是从第0位匹配， serch不按位置匹配

