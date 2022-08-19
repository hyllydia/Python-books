#coding:utf-8
#4-3
print("4-3")
for i in range(1,21):
    print(i)
#4-4
# print("4-4")
# num = list(range(1,10000001))
# for i in num:
#     print(i)
#4-5
print("4-5")
num = list(range(1,10000001))
print(min(num))
print(max(num))
print(sum(num))
#4-6
print("4-6"+ "打印奇数")
odd = list(range(1,21,2))
#print(odd)
for i in odd:
    print(i)
#4-7
print("4-7"+"打印3的倍数")
list1 = list(range(3,31,3))
print(list1)
for i in list1:
    print(i)
#4-8
print("4-8")
list2 = []
for i in range(1,11):
    list2.append(i**3)
print(list2)
for j in list2:
    print(j)

#4-9
print("4-9"+"列表生成式")
list3 = [i**3 for i in range(1,11)]
print(list3)


