#coding:utf-8
names=['lily','jenny','judy']
ages=[20,21,22]
for name,age in zip(names,ages):
    print(name +" is "+str(age)+" years old.")

print(list(zip(names,ages)))
print(list(zip(range(5),range(1,6))))
