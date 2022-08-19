#Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
#coding:utf-8
import re
def string_contain_char(string):
    patten=re.compile(r'^[0-9a-zA-Z]')
    string=patten.search(string)
    return bool(string)

if __name__=="__main__":
    print(string_contain_char("ABDCRGBI9790779"))
    print(string_contain_char("$%^&*(&^%$#$%^rtyujgh"))