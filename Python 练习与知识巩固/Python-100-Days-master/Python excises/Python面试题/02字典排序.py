'''
现有字典d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}，如何按字典中的值对字典进行排序得到排序后的字典。
'''
def sort_d(d):
    new_d=dict(sorted(d.items(),key=(lambda x:x[1]),reverse=True))
    return new_d
if __name__=="__main__":
    d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
    print(sort_d(d))


# Tips: sorted()返回的是一个列表， 所以在前面加上dict()
#     遍历字典的时候需要用d.items()读取的是字典的key, value值
