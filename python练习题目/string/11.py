#coding:utf-8
#Write a Python program to remove the characters which have odd index values of a given string.
def remove_odd_index(str1):
    str2=''
    for i in range(len(str1)):
        if i%2  == 0:
            str2=str2+str1[i]
    return str2

if __name__ == "__main__":
    str_res=remove_odd_index("abcdefg")
    print(str_res)
