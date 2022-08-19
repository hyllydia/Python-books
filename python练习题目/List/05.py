#coding:utf-8
def find_str(list1):
    #list2=[]
    count=0
    for i in range(len(list1)):
        if list1[i][0]==list1[i][-1]:
            #list2.append(list1[i])
            count+=1
    #return len(list2)
    return count
if __name__=="__main__":
    n=find_str(['abc', 'xyz', 'aba', '1221','22','33'])
    print(n)