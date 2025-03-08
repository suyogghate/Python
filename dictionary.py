# Dictionaries
# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.
# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info)

# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info['name'])
# print(info.get('eligible'))

# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info.values())

# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info.keys())

# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info.items())

# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}")

# for key, value in info.items():
#   print(f"The value corresponding to the key {key} is {value}") 

# Dictionary methods------------------------------
# update()
# The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info)
# info.update({'age':20})
# info.update({'DOB':2001})
# print(info)

# clear(): The clear() method removes all the items from the list.
# info = {'name':'Karan', 'age':19, 'eligible':True}
# info.clear()
# print(info)

# pop(): The pop() method removes the key-value pair whose key is passed as a parameter.
# info = {'name':'Karan', 'age':19, 'eligible':True}
# info.pop('eligible')
# print(info)

# popitem(): The popitem() method removes the last key-value pair from the dictionary.
# info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
# info.popitem()
# print(info)

# del: we can also use the del keyword to remove a dictionary item.
# info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
# del info['age']
# print(info)
# If key is not provided, then the del keyword will delete the dictionary entirely.
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)