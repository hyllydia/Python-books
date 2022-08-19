#coding:utf-8
#Write a Python program to check if a string contains all letters of the alphabet.
def check(str):
    s1=set(str.lower())
    print(s1)
    s2=set((''.join(chr(ord('A')+i) for i in range(26))).lower())
    print(s2)
    if s1>=s2:
        return True
    else:
        return False
if __name__=="__main__":
    str1='abca'
    print(check(str1))
    str2='ABCDEFGHIJKLMNOPQRSTUVWXYZbnc'
    print(check(str2))
    str3='The quick brown fox jumps over the lazy dog'
    print(check(str3))
# import string
# alphabet = set(string.ascii_lowercase)
# print(alphabet)
# input_string = 'The quick brown fox jumps over the lazy dog'
# print(set(input_string.lower()) >= alphabet)
# input_string = 'The quick brown fox jumps over the lazy cat'
# print(set(input_string.lower()) >= alphabet)