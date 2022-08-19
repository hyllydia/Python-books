#coding:utf-8
# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the editor
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
#find方法找到的是字符的index, 找到返回第一个字符索引， 找不到返回-1
def change_words(str1):
    n1=str1.find('not')
    n2=str1.find('poor')
    if n1!=-1 and n2!=-1 and n2>n1:
        str1=str1.replace(str1[n1:n2+4],'good')
    return str1
if __name__=="__main__":
    str_res1=change_words('The lyrics is not that poor!')
    print(str_res1)
    str_res2=change_words('The lyrics is poor!')
    print(str_res2)
