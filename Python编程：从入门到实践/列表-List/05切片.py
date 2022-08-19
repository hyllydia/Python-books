#coding:utf-8
#4-10
print("4-10")
food=["Milk Tea","Bread","Snacks","Candy","Chocolate"]
print("The first three items in this list are:")
for item in food[:3]:
    print(item)
print("Three items from the middle of this list are:")
for item in food[1:4]:
    print(item)
print("The last three items in this list:")
for item in food[-3:]:
    print(item)
#start,end,step
print(food[1::2])
#4-11
print("4-11")
food=["Milk Tea","Bread","Snacks","Candy","Chocolate"]
friend_food=food[:]
food.append("ice cream")
friend_food.append("cake")
print("my favourite foods are:")
for item in food:
    print(item)
print("my friend favourite foods are:")
for item in friend_food:
    print(item)
#4-12
print("4-12")
print("pass")
#4-13
print("4-13"+" tuple")
food=("Milk Tea","Bread","Snacks","Candy","Chocolate")
for item in food:
    print(item)
#food[0]= "peach"
#print(food[0])
print("***")
food=("Milk Tea","Bread","ice cream","Candy","cake")
for item in food:
    print(item)
