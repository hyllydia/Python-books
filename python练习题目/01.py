#coding:utf-8
# def result():
#     #0 是 False
#     n=[5,'',None,0,True,False].count(False)
#     print(n)
# if __name__=="__main__":
#     result()

#列表
# a=[1,2,3,4,5]
# a[2:4]=[[9]]
# print(a)

#字典
# d={'name':'xufive'}
# print(d['name'])
# print(d.get('name'))
# print(d.get('age')) #None
# #print(d.name)
# #AttributeError: 'dict' object has no attribute 'name'

#元祖
# a=(1,2)
# b=(3,4)
# print(a[1]==b[0])
# print(a+b)
# print(a)
# print(*a)
# print((a,b))
# print((*a,*b))
# print((2*a,2*b))

#深浅copy()
# import copy
# a=[1,2,[3,4]]
# b=a.copy()
# c=copy.deepcopy(a)
# a[0]=10
# #a[2].append(5)
# # print(b)
# # print(c)
# #a[2][0]=9
# # print(b)
# # print(c)
# #a.append(80)
# print(a)
# print(b)
# print(c)

#三元表达式
# a = [i if i%2 else i*2 for i in range(5)]
# print(a)
# print(3%2)
# c= [i for i in range(5) if i%2]
# print(c)
# a=[]
# for i in range(5):
#     if i%2:
#         #i=i%2
#         a.append(i)
#     else:
#         i=i*2
#         a.append(i)
# print(a)
# str1=''.join(map(lambda s:s*2, 'abc'))
# print(str1)
#
#切片
# num=[1,2,3,4,5]
# print(num[2:4])
# print(num[2:])
# 
# print(num[:-1])
# print(num[-3:-1])
# 
# print(num[:])
# 
# print(num[::-1])
# print(num[::-2])
# 
# print(num[4:1:-1])

#字符串join
# print("*".join("abc"))
# print('*'.join(map(lambda s:s*2, 'abc')))
# s1='a','b','c'
# s2='+'
# print(s2.join(s1))

#同时赋值
# values=1,2,3
# print(values)

#字符串 比较， 字符比大小
# print(ord('A'))
# print(chr(97))
#
# str='I am a great person!'
# print(str.split())
# print(list(str))

# l1=['a','b','c']
# s1='abc'
# str1=''.join(l1)
# print(str1)
# str2='*'.join(s1)
# print(str2)
def reverse_int():
    n = 123
    l1=list(str(n))
    l2=list(reversed(l1))
    if l2==l1:
        return True
    else:
        return False
if __name__=="__main__":
    res=reverse_int()
    print(res)

