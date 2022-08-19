#coding:utf-8
print('9-1')
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("Restaurant name is: "+self.restaurant_name)
        print("Cuisine type is: "+self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name+" is opening!")
if __name__=="__main__":
    rest1 =Restaurant('rongliji','chuancai')
    rest1.describe_restaurant()
    rest1.open_restaurant()

print("9-3")
class User():
    def __init__(self,first_name,last_name,location):
        self.first_name=first_name
        self.last_name=last_name
        self.location=location
    def describe_user(self):
        print("My name is "+self.first_name+' '+self.last_name+", I am from "+self.location+".")
    def greet_user(self):
        print("Hello, "+self.first_name+' '+self.last_name+".")
if __name__=="__main__":
    user1=User('you','Hou','shanghai')
    user1.describe_user()
    user1.greet_user()