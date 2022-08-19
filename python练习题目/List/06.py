#coding:utf-8
# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# def last(n):
#     return n[-1]
#!!!!!sorted()函数中的形参key是指在进行比较之前每个元素上调用的函数，因此传入的参数是列表元素。
def sort_t(list1):
    list2=sorted(list1,key=lambda n:n[-1],reverse=True)
    return list2
if __name__=="__main__":
    l1=sort_t([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
    print(l1)