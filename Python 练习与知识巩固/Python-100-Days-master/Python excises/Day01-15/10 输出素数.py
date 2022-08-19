#coding:utf-8
# 说明：素数指的是只能被1和自身整除的正整数（不包括1）。
#输出100以内所有的素数。

for i in range(2,100):
    is_prime=True
    for j in range(2,i):
            if i%j==0:
                is_prime=False
                break
    if is_prime:
        print(i,end=' ')
#print(l)
"""
输出2~99之间的素数
Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

# import math
#
# for num in range(2, 100):
#     is_prime = True
#     for factor in range(2, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=' ')