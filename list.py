# list1 = [1, 2, 2, 3, 4, 5, 6, 7]
# list2 = ["Red", "Green", "Blue"]
# print(list1)
# print(list2)

# details = ["Abhijeet", 18, "FYBScIT", 9.8]
# print(details)

# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
# print(colors[2])
# print(colors[4])
# print(colors[0])

# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
# print(colors[-1])
# print(colors[-3])
# print(colors[-5])

# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# if "Green" in colors:
#     print("Green is present.")
# else:
#     print("Green is absent.")

# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[3:7])	#using positive indexes
# print(animals[-7:-2])	#using negative indexes'

# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[4:])	#using positive indexes
# print(animals[-4:])	#using negative indexes

# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[:6])	#using positive indexes
# print(animals[:-3])	#using negative indexes

# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[::2])		#using positive indexes
# print(animals[-8:-1:2])	#using negative indexes

# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[1:8:3])


# List Comprehension----------------------------
# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_O = [item for item in names if "o" in item]
# print(namesWith_O)

# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_O = [item for item in names if (len(item) > 4)]
# print(namesWith_O)

# List Methods------------------
# colors = ["voilet", "indigo", "blue", "green"]
# colors.sort()
# colors.sort(reverse=True)      # if you want to sort in descending order
# print(colors)

# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.sort()
# num.sort(reverse=True)
# print(num)

# colors = ["voilet", "indigo", "blue", "green"]
# colors.reverse()      # reverses the order of the list
# print(colors)

# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.reverse()
# print(num)

# colors = ["voilet", "green", "indigo", "blue", "green"]
# print(colors.index("green"))  # This method returns the index of the first occurrence of the list item.

# num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
# print(num.index(3))

# colors = ["voilet", "green", "indigo", "blue", "green"]
# print(colors.count("green"))   # Returns the count of the number of items with the given value.

# num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
# print(num.count(2))

# colors = ["voilet", "green", "indigo", "blue"]
# newlist = colors.copy()   # Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
# print(colors)
# print(newlist)

# colors = ["voilet", "indigo", "blue"]
# colors.append("green")   # This method appends items to the end of the existing list.
# print(colors)

# colors = ["voilet", "indigo", "blue"]
# colors.insert(1, "green")   # This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.
# print(colors)

#add a list to a list
# colors = ["voilet", "indigo", "blue"]
# rainbow = ["green", "yellow", "orange", "red"]
# colors.extend(rainbow)
# print(colors)
# This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)
# You cqn simply concatenate two lists to join two lists.