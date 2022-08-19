#coding:utf-8
#Write a Python program to count repeated characters in a string. Go to the editor
#Sample string: 'thequickbrownfoxjumpsoverthelazydog'
def count_chars(str1):
    d={}
    for i in str1:
        cn=str1.count(i)
        if cn>1:
            d[i]=cn
    return d
if __name__=="__main__":
    str1='thequickbrownfoxjumpsoverthelazydog'
    print(count_chars(str1))