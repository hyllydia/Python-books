#coding:utf-8
#5-1
print("5-1")
food = "cake"
print("Is food ='cake',True of False?")
print(food == 'cake')

print("Is food = 'ice cream',True or false?")
print(food=='ice cream')

#5-2
print("5-2")
str1 = 'Peach'
str2 = "pear"
str3 = "Peach"
print(str1==str2)
if str1 == str3:
    print(str1.lower())
#5-5
print("5-5")
alien_color='green'
if  alien_color == 'green':
    print("You get 5 points!")
elif alien_color == 'yellow':
    print("You get 10 points!")
elif alien_color == 'red':
    print("you get 15 points!")

#5-7
print("5-7")
Fruit=['apple','peach','pear','banana']
if 'apple' in Fruit:
    print("I really love apple!")
if "berry" not in Fruit:
    print("I do not love berry!")

#5-8
print('5-8')
users= ['admin','lily','lucy','eric']
for user in users:
        if user == 'admin':
            print("Hello admin , would you lik to see a status report!")
        elif user == 'lily':
            print("Hello " + user.title()+", thank you for logging!")
#5-9
print("5-9" + "判断空列表")
#users= ['admin','lily','lucy','eric']
users=[]
if users:
    for i in range(len(users)):
        users.pop()
else:
    print("we need to find some users!")
print(users)

#5-10
print("5-10")
print("比较字符串不区分大小写， 运用列表生成式")
current_users=['andy','coco','doris','eric','frank']
new_users=['andy','blair','emily','Frank','flex']
for user in new_users:
    if user.lower() in [current_user.lower() for current_user in current_users]:
        print('"' +user+ '"'+" is already exist,please login with other users!")
    else:
        print('"' +user+ '"' " has not been used!")

#5-11
print("5-11")
num_list=list(range(1,10))
for i in num_list:
    if i==1:
        print(str(1)+"st")
    elif i==2:
        print(str(2)+'nd')
    elif i==3:
        print(str(3)+'rd')
    else:
        print(str(i)+'th')
        




