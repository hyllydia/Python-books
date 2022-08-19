#coding:utf-8
# print("7-4")
# while True:
#     prompt=input("please tell me what kind of pizza ingredients you would like: ")
#     if prompt!='quit':
#         print("I will add "+prompt+" for your pizza.")
#     else:
#         break
print('7-5')
Flag=True
while Flag:
    age="How old are you?"
    age=input(age)
    age=int(age)
    if age<3:
        print("Free")
    elif age>=3 and age<=12:
        print("10 dollars")
    else:
        print("15 dollars")





