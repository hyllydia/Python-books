#coding:utf-8
#Write a Python script to check whether a given key already exists in a dictionary.
def key_in(n,d):
    if n in d.keys():
        print("already exist")
    else:
        print("new key")
if __name__=="__main__":
    d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    key_in(10,d)
    key_in(2,d)