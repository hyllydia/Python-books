#coding:utf-8
print("6-1")
jenny={
    "first_name":'jenny',
    "last_name":"Wang",
    "age":20,
    "city":"shanghai"
}
for k,v in jenny.items():
    if type(v) is not str:
        print(k + ":" + str(v))
    else:
        print(k+":"+v)

print("6-2")
favorite_num={
    'allen':7,
    'blair':3,
    'clank':5,
    'doris':8
}
for name,value in favorite_num.items():
    print(name.title()+" favorite number is " + str(value))

print("6-3")
favorite_language={
    'allen':'C++',
    'blair':'python',
    'clank':'Perl',
    'doris':'php'
}
for name ,value in favorite_language.items():
    print(name.title()+"favorite number is: \n" + value.title())