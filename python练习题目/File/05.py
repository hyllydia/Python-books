#coding；utf-8
#Write a Python program to count the number of lines in a text file.
filename='01.txt'
with open(filename,'r') as fp:
    contents=fp.read().split()
    print(len(contents))