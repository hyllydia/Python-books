#coding:utf-8
# Write a Python function that takes a list of words and returns the longest word and the length of the longest one. Go to the editor
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9
import heapq
def longest_words(l1):
    # lw=''.join(heapq.nlargest(1,l1))
    # return lw
    #答案
    l2=[]
    for i in l1:
        l2.append((len(i),i))
    l3=sorted(l2)
    lw=l3[-1][1]
    return lw
if __name__=="__main__":
    l1=['abc','lydia','lydia','strawberry']
    lw=longest_words(l1)
    print("Longest word: " +lw)
    print("Length of longest word: " +str(len(lw)))