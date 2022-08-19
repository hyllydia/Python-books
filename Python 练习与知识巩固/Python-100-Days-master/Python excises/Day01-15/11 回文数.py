#coding:utf-8
def is_palindrome(num):
    nl=list(str(num))
    #print(nl)
    nl_r=list(reversed(nl))
    #print(nl_r)
    if nl==nl_r:
       print ((''.join(nl))+" is a palindrome!")
       return (num)
    else:
        print("This num is not palindrome!")
        return None
if __name__=="__main__":
    num=int(input("please input a num:"))
    print(is_palindrome(num))

