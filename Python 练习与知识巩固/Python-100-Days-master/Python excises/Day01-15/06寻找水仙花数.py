#coding:utf-8
#说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
# 它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
# for n in range(100,1000):
#     nl=list(str(n))
#     num =0
#     for i in nl:
#         num +=int(i)**3
#     if num==n:
#         print(str(n)+" is the num I found!")

#通过整除和求模运算找出三位数的个位，十位，百位
for n in range(100,1000):
    low=n % 10
    mid= n // 10 % 10
    high= n //100
    if n == low**3+mid**3+high**3:
        print(n)