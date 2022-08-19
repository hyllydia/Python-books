#coding:utf-8
'''
编写一小段程序，利用for 循环，打印出从1 到10 的数字。然后利用while
循环，编写一个等价的程序，打印出从1 到10 的数字
'''
def for_fab():
    for i in range(1,11):
        print(i)
def while_fab():
    i=1
    while True:
        print(i)
        i+=1
        if i>10:
            break
if __name__=="__main__":
    for_fab()
    while_fab()