#coding:utf-8
#Write a python program to find the longest words.
filename='01.txt'
# lf=[]
with open(filename,'r') as fp:
    contents=fp.read().split()
    print(contents)
#max_len=len(max(lf,key=len))
#print([word for word in lf if len(word)==max_len])
max_len=len(max(contents,key=len))
print([word for word in contents if len(word)==max_len])