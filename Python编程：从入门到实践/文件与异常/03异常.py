#coding:utf-8
# print('10-6')
# def add(a,b):
#     # try:
#     #     c=int(a+b)
#     # except:
#     #     print('error')
#     # else:
#     #     print(c)
#     c=a+b
#     print(c)
#
# if __name__=="__main__":
#     while True:
#         try:
#             a = input('input a number:')
#             b = input('input a number:')
#             a=int(a)
#             b=int(b)
#         except ValueError:
#             print("Please input int type!")
#         else:
#             add(a,b)

print('10-8')
# def create_files():
#     with open('cats.txt','w') as f:
#         f.write("coco\n")
#         f.write('bobo\n')
#         f.write('tianmao')
#     with open('dogs.txt','w') as f:
#         f.write('jing\n')
#         f.write('dong\n')
#         f.write('kiki')
def read_file(file):
    try:
        with open(file,'r') as f:
            contents=f.read()
    except FileNotFoundError:
        print("This file does not exist!")
    else:
        print(contents.split())
        len_file=len(contents.split())
        print("This file has "+ str(len_file)+" words!")
if __name__=="__main__":
    files=['dogs.txt','cats.txt','sheep.txt']
    for file in files:
        read_file(file)
    #create_files()

print('10-10')
def count_words(file):
    try:
        with open(file,'r') as f:
            contents=f.read()
    except FileNotFoundError:
        print("This file does not exist!")
    else:
        m=contents.lower()
        n=m.count('python')
        print(n)

if __name__=="__main__":
    files=['learning_python.txt','guest_users.txt']
    for file in files:
        count_words(file)
