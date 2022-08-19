#coding:utf-8
#两种方法， 一种用数学求模运算， 另外一种转换成字符串，再转换成列表反转，
#列表的反转方式有三种：l.reverse(), list(reversed(l)),l_new=l[::-1]
def reverse_num(num):
    new_num=0
    while num>0:
        new_num= new_num*10 + num%10
        num //=10
    print(new_num)
def reverse_num1(num):
    num_sl=list(str(num))
    #re_l=list(reversed(num_sl))
    #num_sl.reverse()
    re_sl=num_sl[::-1]
    new_num = int("".join(re_sl))
    print(new_num)
if __name__=="__main__":
    while True:
        num0 = input("Please input a num:")
        print("Enter 'q'to exit!")
        if num0 =='q':
            break
        else:
            try:
                num = int(num0)
                if num>0:
                    reverse_num1(num)
                else:
                    print("please input a num>0!")
            except ValueError:
                print("Please input a int type!")



