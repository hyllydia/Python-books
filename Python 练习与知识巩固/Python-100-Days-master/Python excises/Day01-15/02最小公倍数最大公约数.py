#coding:utf-8
def gcd(a,b):
    #最大公约数--greatest common divisor
    (a,b)=(a,b) if a<b else (b,a)
    for i in range(a,0,-1):
        if a % i == 0 and b % i == 0:
            return i
def lcm(a,b,c):
    #最小公倍数-least common multiple
    m=a*b//c
    return m

if __name__=="__main__":
    a=int(input("please input a num:"))
    print(type(a))
    b=int(input('please input a num:'))
    gcd_num = gcd(a,b)
    print("greatest common divisor:"+str(gcd_num))
    lcm_num=lcm(a,b,gcd_num)
    print("least common multiple: "+str(lcm_num))


