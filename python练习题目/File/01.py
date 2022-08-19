#coding:utf-8
filename='01.txt'
#读取整个文件
# with open(filename,'r') as fp:
#     # contents=fp.read()
#     # print(type(contents))
#     # print(contents)
#
#     contents=fp.readlines()
#     print(type(contents))
#     #print(contents)
#     for item in contents:
#         print(item.rstrip())

#读取前几行
# def read_firstlines(n):
#     with open(filename,'r') as fp:
#         lines=fp.readlines()
#         for line in lines[:n]:
#             print(line)
# if __name__=="__main__":
#     read_firstlines(2)

#读取后几行
def read_firstlines(n):
    with open(filename,'r') as fp:
        lines=fp.readlines()
        for line in lines[-1-n:]:
            print(line)
if __name__=="__main__":
    read_firstlines(3)
