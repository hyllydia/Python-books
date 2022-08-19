#coding:utf-8
# # Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
# Sample String : 'restart'
# Expected Result : 'resta$t'
def replace_fir(str1):
    char=str1[0]
    for i in str1:
        if i==char:
            str1=str1.replace(i,'$')
    str1=char+str1[1:]
    print(str1)

if __name__=="__main__":
    replace_fir("rastartr")