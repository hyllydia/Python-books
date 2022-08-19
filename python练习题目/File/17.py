#coding:utf-8
#Write a Python program to remove newline characters from a file 删除文件中的换行符
#newline characters ----换行符
# def remove_newlines(fname):
#     flist = open(fname).readlines()
#     return [s.rstrip('\n') for s in flist]
#
# print(remove_newlines("01.txt"))

filename='02.txt'
with open(filename,'r') as fp:
    lines=fp.readlines()
    print(lines)
    print([line.rstrip() for line in lines])

