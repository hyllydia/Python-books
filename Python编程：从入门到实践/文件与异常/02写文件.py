#coding:utf-8
print('10-3')
def guest_users():
    while True:
        message=input("Before guesting please input your name:")
        print("Enter 'q' to exit!")
        if message=='q':
            break
        else:
            #w模式会将文件清空重新写入，a附加模式是在原来的内容末尾添加
            with open('guest_users.txt', 'a') as f:
                f.write(message+'\n')
                f.write('Welcome '+message+"!\n")
if __name__=="__main__":
    guest_users()