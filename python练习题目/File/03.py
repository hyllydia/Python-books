#coding:utf-8
#Write a Python program to read a file line by line and store it into a list. G
filename="01.txt"
lf=[]
with open(filename,'r') as fp:
    lines=fp.readlines()
    print(lines)
    for line in lines:
        lf.append(line.rstrip())
#         #去除文件中自带的换行符，用rstrip()!!!!
print(lf)
#若要去掉文件中自带的换行，line.rstrip() 去除空白字符。空白符（包括'\n', '\r', '\t', ' ')