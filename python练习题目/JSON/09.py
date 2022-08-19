import json
json_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
print("Original json object:")
print(json_obj)
python_obj = json.loads(json_obj)
print("\nUnique Key in a python object:")
print(python_obj)
print(type(python_obj))

d={
    'a':1,
    'a':'obj',
    'a':3
}
print(d)

json_o='{"a":2, "a":"obj"}'
print(json_o)