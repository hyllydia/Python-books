#coding:utf-8
#Write a Python program that takes a text file as input and returns the number of words of a given text file
filename='02.txt'
def count_words(file):
    lf=[]
    with open(file,'r') as fp:
        contents=fp.read().split()
        print(contents)
        for item in contents:
            if ',' in item:
                lm=item.split(',')
                for i in range(len(lm)):
                    lf.append(lm[i])
            else:
                lf.append(item)
        print(lf)
        print(len(lf))
        #没有考虑到换行符
        # contents=fp.read()
        # new_c=contents.replace(",",' ').rstrip('\n')
        # print(new_c.split(" "))
        # print(len(new_c.split(" ")))


if __name__=="__main__":
    count_words('02.txt')