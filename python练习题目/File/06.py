# Write a Python program to count the frequency of words in a file.
#coding:utf-8
filename='01.txt'
with open(filename,'r') as fp:
    words=fp.read().split()
    for word in words:
        c=words.count(word)
        print(word+": "+ str(c))