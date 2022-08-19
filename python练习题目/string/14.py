#coding:utf-8
#Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). Go to the editor
#Sample Words : red, white, black, red, green, black
#Expected Result : black, green, red, white,red
def sorted_words(str):
    l1=str.split(',')
    print(l1)
    s2=set(l1)
    print(s2)
    str_res=','.join(sorted(list(s2)))
    return str_res
if __name__=="__main__":
    print(sorted_words('red, white, black, red, green, black'))