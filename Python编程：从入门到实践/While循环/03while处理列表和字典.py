#coding:utf-8
# print("7-8")
#drinks_order=['cola','milk','tea','juice']
#drinks_finished=[]
# while drinks_order:
#     new_drink=drinks_order.pop()
#     print("I made your "+new_drink+".")
#     drinks_finished.append(new_drink)
# print(drinks_finished)

print("7-9")
drinks_order=['cola','milk','tea','juice','cola','cola']
drinks_finished=[]
print("cola is sold out!")
while 'cola' in drinks_order:
    drinks_order.remove('cola')
while drinks_order:
    new_drink = drinks_order.pop()
    print("I made your " + new_drink + ".")
    drinks_finished.append(new_drink)
print(drinks_finished)

# print("7-10")
# info={}
# while True:
#     name=input("What is your name?")
#     if name == 'None':
#         break
#     place = input("If you could visit one place in the world, where would you go? ")
#     info[name] =place
# print(info)




