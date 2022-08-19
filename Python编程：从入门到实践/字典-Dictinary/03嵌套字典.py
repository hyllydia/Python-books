#coding:utf-8
print("6-7")
people={
    'jenny' : {
    "first_name": 'jenny',
    "last_name": "Wang",
    "age": 20,
    "city": "shanghai"
},
    'lucy':{
    "first_name": 'lucy',
    "last_name": "li",
    "age": 18,
    "city": "wuhan"
    }
}
for name,info in people.items():
    print(name.title() +"'s info is:")
    Full_name=info['first_name']+info['last_name']
    Age=info['age']
    Location=info['city']
    print("Full name: " +Full_name )
    print("Age: "+ str(Age))
    print("Location: "+Location)

print("6-8"+"字典列表")
coco={
    'pet_type':'pig',
    'master':'allen'
}
oscar={
    'pet_type':'dog',
    'master':'jenny'
}
candy={
    'pet_type':'cat',
    'master':'frank'
}
pets=[coco,oscar,candy]
for pet in pets:
    print(pet)

print("6-9"+"字典包含列表")
favorite_places={
    'jenny':['shanghai','london','paris'],
    'eric':['shanghai','beijing'],
    'flex':['beijing','london']
}
for name,place in favorite_places.items():
    print(name.title() +"'s favrite places is:")
    for city in place:
        print(city.title())

print("6-11"+"列表嵌套列表")
cities={
    'shanghai':{
        'location':'east',
        'people': 2000
},
    'beijing':{
        'location':'north',
        'people': 3000
    }
}
for city,infoes in cities.items():
    print(city.title()+"'s info is:")
    #for k,v in infoes.items():
    print('Location:'+infoes['location'])
    print('People:' + str(infoes['people'])+'W')