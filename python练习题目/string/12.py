#coding:utf-8
# Write a Python program to count the occurrences of each word in a given sentence
def count_words(word,s1):
    l1=s1.lower().split(' ')
    n=l1.count(word)
    return n
if __name__=="__main__":
    s1="Your favorite fruit is apple , you like apple pie . You like apple wine ."
    res1=count_words('apple',s1)
    print(res1)
    res2=count_words('you',s1)
    print(res2)