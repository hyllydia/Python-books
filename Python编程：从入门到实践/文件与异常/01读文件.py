#coding:utf-8
print('10-1')
# with open('learning_python','r') as f:
#     contents = f.read()
#     print(contents)
# with open('learning_python', 'r') as f:
#     for line in f:
#         print(line.rstrip())
with open('learning_python','r') as f:
    lines=f.readlines()
for line in lines:
    print(line.rstrip())

print('10-2')
with open('learning_python','r') as f:
    lines=f.readlines()
for line in lines:
    print(line.replace('python','C').rstrip())