#coding:utf-8
#3-8
""""
方法sort(),reverse()永久性的修改列表元素的排列顺序
方法sorted()可以以特定的顺序呈现，同时不改变列表原始顺序
"""
print("3-8")
places = ["Paris","London","Shanghai","Tibet","Lijiang"]
print("原始列表:")
print(places)
print("sorted 之后的列表：")
print(sorted(places))
print(places)
print("sorted并顺序相反打印列表：")
print(sorted(places,reverse=True))
print(places)
print("reverse修改列表：")
places.reverse()
print(places)
print("再次reverse就可以恢复列表：")
places.reverse()
print(places)
print("sort修改列表：")
places.sort()
print(places)
print("sort修改列表并顺序相反打印列表：")
places.sort(reverse=True)
print(places)
#3-9
print("3-9")
print(len(places))
#3-10
print("3-10")
food=["Milk Tea","Bread","Snacks","Candy","Chocolate"]
print(food)
food[0]="Apple"
print(food)
food.insert(2,"Peach")
print(food)
food.append("Pear")
print(food)
del food[1]
print(food)
pop_food=food.pop()
print(pop_food)
print(food)
food.remove("Peach")
print(food)

print("*****")
food=["Milk Tea","Bread","Snacks","Candy","Chocolate"]
food.sort()
print(food)
food.sort(reverse=True)
print(food)
print("*****")
food=["Milk Tea","Bread","Snacks","Candy","Chocolate"]
print(sorted(food,reverse=True))
print(len(food))


print(list(enumerate(food,start=1)))