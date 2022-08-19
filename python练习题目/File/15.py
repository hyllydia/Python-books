#codingcoding:utf-8
#Write a Python program to assess if a file is closed or not.
f=open('01.txt')
print(f.closed)
f.close()
print(f.closed)