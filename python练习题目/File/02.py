#coding:utf-8
#Write a Python program to append text to a file and display the text.
filename='01.txt'
with open(filename,'a+') as fp:
    fp.write("\npython")
with open(filename,'r') as fp:
    contents=fp.read()
    print(contents)