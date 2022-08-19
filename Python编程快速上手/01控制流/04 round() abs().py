#coding:utf-8
#round()对浮点数近似取值
# round(n,r)函数的结果是四舍五入保留数值n的小数点的后r位，参数r可以省略，在这种情况下，n将四舍五入为整数。
# 当数字n是两个相邻整数的中间值（例如1.5，2.5，3.5和4.5）时，round函数将返回与其最为接近的偶数。
# 例如round(2.1)的结果是2，round(3.5)的结果是4。
print(round(2.1))
print(round(2.6))
print(round(2.3178,2))
print(round(2.3178,1))
#abs()用于取绝对值
#abs(x)绝对值函数就是|x|。该函数将负数中的负号去掉并保持其他部分不变。
# 数值的绝对值和复数的幅值
print(abs(-3))

print(abs(4+3j))
#abs(4+3j)=sqrt(4*4+3*3)