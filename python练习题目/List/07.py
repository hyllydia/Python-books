#coding:utf-8
# Write a Python program to remove duplicates from a list
def remove_dup(l1):
    dup_list=set()
    unique_list=[]
    for i in l1:
        if i in unique_list:
            dup_list.add(i)
        else:
            unique_list.append(i)
    return unique_list
if __name__=="__main__":
    l1=[1,2,2,3,5,4,3,3,44,5]
    l2=remove_dup(l1)
    print(l2)
    #print(list(set(l1)))