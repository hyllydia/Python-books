#coding:utf-8

def max_nums(list_num):
    m1,m2= (list_num[0],list_num[1]) if list_num[0]>list_num[1] else (list_num[1],list_num[0])
    for i in range(2,len(list_num)):
        if list_num[i]>m1:
            m2 =m1
            m1=list_num[i]
        elif list_num[i]>m2:
            m2=list_num[i]
    return m1,m2

if __name__== "__main__":
    list1=[1,2,10,4,60]
    m1,m2=max_nums(list1)
    print("列表中最大元素和第二大元素是：{},{}".format(m1,m2))

import heapq

if __name__=="__main__":
    list1=[200,107,300,409,20,13]
    print(heapq.nlargest(2,list1))
    print(heapq.nsmallest(2,list1))