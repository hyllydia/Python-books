#coding:utf-8
#Write a Python program to combine each line from first file with the corresponding line in second file
filename1='01.txt'
filename2='02.txt'
def combine_line():
    with open(filename1,'r') as f1,open(filename2,'r') as f2:
        for line1,line2 in zip(f1,f2):
            print (line1.rstrip()+"-"+line2.rstrip())
if __name__=="__main__":
    print(combine_line())