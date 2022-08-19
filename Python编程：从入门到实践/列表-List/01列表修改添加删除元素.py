#coding:utf-8
#3-1
print("3-1")
names = ["andy","lily","jenny"]
print(names[0])
print(names[1])
print(names[2])
#3-2
print("3-2")
for i in range(len(names)):
    message = "hello " + names[i] +"!"
    print(message)
#3-3
print("3-3")
traffic_way =["train","car","bicycle"]
for i in range(len(traffic_way)):
    message = "I would like to work by " + traffic_way[i] + "!"
    print(message)
#3-4
print("3-4" + "\npass")
#pass
#3-5
print("3-5")
print(names[-1] + " would not come to the party!")
names[-1] = "judy"
print("I have updated the girls who will join the party!")
for i in range(len(names)):
    print(names[i] + " would like to come to my party!")
#3-6
print("3-6")
print("I will invite more friends to my party!")
names.insert(0,"ming")
names.insert(2,"jim")
names.append("Kris")
for i in range(len(names)):
    print(names[i] + " would like to come to my party!")
#3-7
print("3-7")
print("Sorry to ack you that I just can invite two friends!")
print(names)
ll = len(names)-2
print(ll)
for i in range(ll):
    #print(i)
    '''
    Tips:容易犯错的地方， pop完之后形成一个新的列表，
    下一次pop从第一个元素开始， index还是0，或者直接不写index，直接pop(),从列表的末尾删除
    '''
    sorry_friend = names.pop()
    print(sorry_friend + " sorry to ack you!")
print(names)
for i in range(len(names)):
    print("Hi " + names[i] + ", I invite you to my party!")
del names[0]
#Tips: 这里也一样，del之后的names只剩下一个元素了，所以names[1]就报错了，还得是names[0]
del names[0]
print(names)

