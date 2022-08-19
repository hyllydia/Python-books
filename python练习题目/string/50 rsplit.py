#coding:utf-8
# Syntax
# string.rsplit(separator, maxsplit)
# Parameter Values
# Parameter 	Description
# separator 	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
# maxsplit 	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
str1="w,3,r,e,s,o,u,r,c,e"
print(str1.rsplit(",",1))
print(str1.rsplit(",",2))
print(str1.rsplit(",",3))