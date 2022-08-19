#coding:utf-8
# Write a Python program to find the first non-repeating character in given string
def find_char(str):
    for i in str:
        if str.count(i)==1:
            return i
if __name__=="__main__":
    print(find_char("abcabc"))