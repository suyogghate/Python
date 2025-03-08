# Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.
# tuple1 = (1,2,2,3,5,4,6)
# tuple2 = ("Red", "Green", "Blue")
# print(tuple1)
# print(tuple2)

# details = ("Abhijeet", 18, "FYBScIT", 9.8)
# print(details)

# country = ("Spain", "Italy", "India", "England", "Germany")
# if "Germany" in country:
#     print("Germany is present.")
# else:
#     print("Germany is absent.")

# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[3:7])     #using positive indexes
# print(animals[-7:-2])   #using negative indexes

# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[4:])      #using positive indexes
# print(animals[-4:])     #using negative indexes

# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[:6])      #using positive indexes
# print(animals[:-3])     #using negative indexes

# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[::2])     #using positive indexes
# print(animals[-8:-1:2]) #using negative indexes

# tup = (1, 2, 45, 78, "green", True)
# tup[0] = 6  # error: 'tuple' object does not support item assignment
# print(tup)
# print(type(tup), tup)
# print(tup[34])

# tup2 = tup[1:4]
# print(tup2)

# Manipulating Tuples---------------------------
# countries = ("Spain", "Germany", "India", "England", "Italy")
# temp = list(countries)
# temp.append("Japan")
# temp.pop(3)
# temp[2] = "Finland"
# countries = tuple(temp)
# print(countries)

# countries = ("Pakistan", "Afghanistan", "Bangladesh", "SriLanka")
# countries2 = ("Vietnam", "India", "China")
# southEastAsia = countries + countries2
# print(southEastAsia)

# Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# res = Tuple1.count(3)
# print('Count of 3 in Tuple1 is:', res)

Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)    #The Index() method returns the first occurrence of the given element from the tuple. 
print('First occurrence of 3 is', res)