#coding：utf-8
# 2. Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

def cha_count(str):
    str1=list(str)
    d={}
    for key in str1:
        d[key]=str1.count(key)
    return d

if __name__=="__main__":
    res=cha_count("google.com")
    print(res)
