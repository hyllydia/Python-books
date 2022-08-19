#coding:utf-8
#返回给定字符串中出现频次最高的字符。

def char(str):
    print(set(str))
    return max(set(str),key=str.count)
if __name__=="__main__":
    print(char('Iama agr eeeee at p e rson!'))
    max()