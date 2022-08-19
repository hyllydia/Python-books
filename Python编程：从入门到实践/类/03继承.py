#coding:utf-8
print('9-6')
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print("Restaurant name is: " + self.restaurant_name)
        print("Cuisine type is: " + self.cuisine_type)

class IceCreamStand():
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=['bingfen','milk']
    def read_icecream(self):
        print("Flavors are: "+str(self.flavors))
if __name__=="__main__":
    icecream=IceCreamStand('rongliji','chuancai')
    icecream.read_icecream()
    #icecream.describe_restaurant()