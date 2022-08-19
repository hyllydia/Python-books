#coding:utf-8
print('9-4')
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type,number_served):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print("Restaurant name is: "+self.restaurant_name)
        print("Cuisine type is: "+self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name+" is opening!")
    def set_number_served(self,number_served):
        self.number_served=number_served
    def read_number_served(self):
        print(self.restaurant_name+" has "+str(self.number_served) +" person to have dinner!")
    def increment_number_served(self,add):
        self.number_served +=add
if __name__=="__main__":
        restaurant=Restaurant('rongliji','chuancai',10)
        #通过修改方法修改属性值
        restaurant.set_number_served(20)
        restaurant.read_number_served()
        #通过方法增加属性值
        restaurant.increment_number_served(15)
        restaurant.read_number_served()
        #直接修改属性值
        restaurant.number_served=30
        restaurant.read_number_served()

print('9-5')
class User():
    def __init__(self,first_name,last_name,logging_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.logging_attempts=logging_attempts
    def increment_login_attempts(self):
        self.logging_attempts+=1
        print("logging_attempts is: "+str(self.logging_attempts))
    def reset_login_attempts(self):
        self.logging_attempts=0
        print("logging_attempts has been reseted: " + str(self.logging_attempts))
if __name__=="__main__":
    user=User('jenny','li',7)
    user.increment_login_attempts()
    user.reset_login_attempts()
