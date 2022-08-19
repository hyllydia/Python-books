#coding:utf-8
#函数不能返回列表，那么可以传递两个列表，其中一个是空列表，处理好的元素放入空列表中
print('8-9')
def show_magicians(magicians):
    for magician in magicians:
        print(magician)
if __name__=="__main__":
    magicians=['allen','blair','coco']
    show_magicians(magicians)

print('8-10')
def make_great(magician):
    modified_magician='the great '+magician +"!"
    return modified_magician
def show_magicians(magicians):
    for magician in magicians:
        print(magician)
if __name__=="__main__":
    magicians=['ming','xiao','xi']
    new_magicians=[]
    for magician in magicians:
        new_magician=make_great(magician)#这里是将每一个列表元素传入函数进行遍历
        #print(new_magician)
        new_magicians.append(new_magician)
    show_magicians(new_magicians)
    show_magicians(magicians)

print('8-10')

def show_magicians(magicians):
    for magician in magicians:
        print(magician)
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i]='the great '+ magicians[i] +'!'
if __name__=="__main__":
    magicians=['allen','blair','coco']
    make_great(magicians)
    show_magicians(magicians)

print('8-11')
def show_magicians(magicians):
    for magician in magicians:
        print(magician)
def make_great(magicians,new_ll):
    for magician in magicians:
        new_magician="the great "+magician +"!"
        new_ll.append(new_magician)
if __name__=="__main__":
    magicians=['allen','blair','coco']
    new_magicians=magicians[:]
    ll=[]
    make_great(new_magicians,ll)#这里是将两个列表传入函数进行遍历处理
    show_magicians(ll)
    show_magicians(magicians)