#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
#coding:utf-8
# import string, os
# if not os.path.exists("letters"):
#    os.makedirs("letters")
# for letter in string.ascii_uppercase:
#    with open(letter + ".txt", "w") as f:
#        f.write(letter)


for letter in [chr(n) for n in range(ord('A'),ord('A')+26)]:
    with open(letter+'.txt','w') as f:
        f.write(letter)
