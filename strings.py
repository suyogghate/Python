# name = "Harry"
# print("Hello, " + name)

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# print(name[0])
# print(name[1])

# for character in name:
#     print(character)

# name = "Harry"
# friend = "Rohan"
# anotherFriend = 'Lovish'
# apple = '''He said, 
# Hi Harry
# hey I am good
# "I want to eat an apple"'''
 
# print("Hello, " + name)
# print(apple) 
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# # print(name[5]) # Throws an error
# print("Lets use a for loop\n")
# for character in apple:
#     print(character)

# String methods
# fruit = "Mango"
# len1 = len(fruit)
# print("Mango is a", len1, "letter  word.")

# pie = "ApplePie"
# print(pie[:5])
# print(pie[6])
# print(pie[5:])
# print(pie[2:6])  # including 2 but not 6
# print(pie[-8:])
# print(pie[:len(pie) - 3])
# print(pie[-3:-1])
# print(pie[-4:-2])
# alphabets = "ABCDEF"
# for i in alphabets:
#     print(i)

# --------------------------------------

# str1 = "AbcDEfghIJ"
# print(str1.upper())
# print(str1.lower())

# str2 = " Silver Spoon "
# print(str2.strip()) # The strip() method removes any white spaces before and after the string.

# str3 = "Hello !!!"
# print(str3.rstrip("!"))  # the rstrip() removes any trailing characters.

# str2 = "Silver Spoon"
# print(str2.replace("Sp", "M"))

# str2 = "Silver Spoon"
# print(str2.split(" "))      #Splits the string at the whitespace " ".

# str1 = "hello"
# capStr1 = str1.capitalize()
# print(capStr1)
# str2 = "hello WorlD"
# capStr2 = str2.capitalize()
# print(capStr2)
# # The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase.

# str1 = "Welcome to the Console!!!"
# print(str1.center(50)) # The center() method aligns the string to the center as per the parameters given by the user.

# str1 = "Welcome to the Console!!!"
# print(str1.center(50, "."))

# str2 = "Abracadabra"
# countStr = str2.count("a") # The count() method returns the number of times the given value has occurred within the given string.
# print(countStr)

# str1 = "Welcome to the Console !!!"
# print(str1.endswith("!!!"))

# str1 = "Welcome to the Console !!!"
# print(str1.endswith("to", 4, 10))

# str1 = "He's name is Dan. He is an honest man."
# print(str1.find("is"))

# str1 = "He's name is Dan. Dan is an honest man."
# print(str1.index("Dan"))
# As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

# str1 = "WelcomeToTheConsole"
# print(str1.isalnum())
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
# str1 = "Welcome"
# print(str1.isalpha())
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

# str1 = "hello world"
# print(str1.islower())

# str1 = "We wish you a Merry Christmas"
# print(str1.isprintable())
# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.

# str1 = "        "       #using Spacebar
# print(str1.isspace())
# str2 = "        "       #using Tab
# print(str2.isspace())

# str1 = "World Health Organization" 
# print(str1.istitle())
# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

# str1 = "WORLD HEALTH ORGANIZATION" 
# print(str1.isupper())

# str1 = "Python is a Interpreted Language" 
# print(str1.startswith("Python"))

# str1 = "Python is a Interpreted Language" 
# print(str1.swapcase())
# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

# str1 = "He's name is Dan. Dan is an honest man."
# print(str1.title())
# The title() method capitalizes each letter of the word within the string.

# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))

# val = 'Geeks'  
# print(f"{val}for{val} is a portal for {val}.")  
# name = 'Tushar'  
# age = 23  
# print(f"Hello, My name is {name} and I'm {age} years old.")

# letter = "Hey my name is {0} and I am from {1}"
# country = "India"
# name = "Harry"

# print(letter.format(name, country))
# print(letter.format(country, name))
# print(f"Hey my name is {name} and I am from {country}")
# print(f"We use f-strings like this: Hey my name is {name} and I am from {country}")

# print(type(f"{2 * 30}"))

# def square(n):
#     '''Takes in a number n, returns the square of n'''
#     print(n**2)

# square(5)
# print(square.__doc__)          # prints the docstring inside a method

# Email slicer program
email = input("Enter your email: ")

# index = email.index("@")

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(f"Your username is {username} and domain is {domain}.")
