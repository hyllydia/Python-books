#coding：uTF-8
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Go to the editor
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
def generate_d(n):
    d={}
    for i in range(1,n+1):
        d[i]=i*i
    return d
    pass
if __name__=="__main__":
    while True:
        num=int(input("please input a number>0: "))
        if num>0:
            d_res=generate_d(num)
            print(d_res)
        else:
            print("Error!")
            break
