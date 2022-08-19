#coding:utf-8
def largest_num(l1):
    # l2=sorted(l1)
    # max=l2[-1]
    # return max
    max=l1[0]
    for i in l1:
        if i>max:
            max=i
    return max
if __name__=="__main__":
    max=largest_num([1, 2, 8,-10])
    print(max)