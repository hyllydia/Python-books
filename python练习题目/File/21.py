# Write a Python program to create a file where all letters of
# English alphabet are listed by specified number of letters on each line.
#coding:utf-8
def create_file(num):
    letters=[chr(n) for n in range(ord('a'),ord('a')+26)]
    with open('new_file','w') as fp:
        for n in range(0,len(letters),num):
            fp.writelines(''.join(letters[n:n+num])+'\n')
if __name__=="__main__":
    create_file(4)