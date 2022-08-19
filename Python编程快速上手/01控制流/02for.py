#在for 循环中，range(10)、range(0, 10)和range(0, 10, 1)之间的区别是什么？
#coding:utf-8
for i in range(10):
    print(i)
print("**")
for i in range(0,10):
    print(i)
print("***")
for i in range(0,10,2):
    print(i)