#coding:utf-8
# Write a Python program to swap comma and dot in a string. Go to the editor
# Sample string: "32.054,23"
# Expected Output: "32,054.23"
# def swap(str1):
#     l1=list(str1)
#     for i,j in enumerate(l1):
#         if j ==',':
#             l1[i]='.'
#         elif j=='.':
#             l1[i]=','
#     return (''.join(l1))
#
# if __name__=="__main__":
#     print(swap('32.054,23.33,098'))

amount = "32.054,23"
maketrans_amount = amount.maketrans(',.', '.,')
amount = amount.translate(maketrans_amount)
print(amount)