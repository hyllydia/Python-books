#coding:utf-8
print('8-12')
def fruit(*args):
    print("Milk with ingredients:")
    for ingredient in args:
        print('-'+ingredient)
if __name__=="__main__":
    fruit('peach')
    fruit('apple','orange')

print('8-13')
def students_info(name,id,**kwargs):
    profile={}
    profile['name']=name
    profile['id']=id
    for k,v in kwargs.items():
        profile[k]=v
    return profile
if __name__=="__main__":
    info=students_info('jenny','000',location='shanghai',address='yangpu',degree='master')
    print(info)

print('8-14')
def make_car(branch,country,**kwargs):
    cars={}
    cars["branch"]=branch
    cars['country']=country
    for k,v in kwargs.items():
        cars[k]=v
    return(cars)
if __name__=="__main__":
    car = make_car('subaru', 'China', color='blue', tow_package=True)
    print(car)