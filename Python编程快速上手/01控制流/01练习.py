#coding:utf-8
'''
编写代码，如果变量spam 中存放1，就打印Hello，如果变量中存放2，就
打印Howdy，如果变量中存放其他值，就打印Greetings!
'''
def value():
    spam = ''
    spam = int(input("Please input spam:"))
    if spam ==1:
        print("Hello")
    elif spam ==2:
        print('Howdy')
    else:
        print('Greetings!')
if __name__=="__main__":
    value()
