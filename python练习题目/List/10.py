#coding:utf-8
# Write a Python program to find the list of words that are longer than n from a given list of words
def find_words(n,str1):
    l1=str1.split(' ')
    l2=[]
    for i in l1:
        if len(i)>n:
            l2.append(i)
    return l2
if __name__=="__main__":
    l1=find_words(3, "The quick brown fox jumps over the lazy dog")
    print(l1)