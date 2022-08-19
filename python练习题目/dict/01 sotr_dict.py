# coding:utf-8
# Write a Python script to sort (ascending and descending) a dictionary by value
import operator
def sort_d():
    d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    print("original dict:",d)
    sorted_d_asc=dict(sorted(d.items(),key=lambda x:x[1]))
    print("ascending dict：",sorted_d_asc)
    sorted_d_des=dict(sorted(d.items(),key=operator.itemgetter(0),reverse=True))
    print("descending dict: ",sorted_d_des)

if __name__=="__main__":
    sort_d()