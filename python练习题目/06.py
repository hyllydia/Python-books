#coding:utf-8
#生成A-Z字符串
s=''.join(chr(ord('A')+i) for i in range(26))
print(s)