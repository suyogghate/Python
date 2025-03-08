# a = int(input("Enter your age: "))
# print("Your age is:", a)
# Conditional operators 
# >, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
# if(a>18):
#   print("Yes, You can drive")
# else:
#   print("No, You cannot drive")

# num = int(input("Enter the value of num: "))
# if (num < 0):
#   print("Number is negative.")
# elif (num == 0):
#   print("Number is Zero.")
# elif (num == 999):
#   print("Number is Special.")
# else:
#   print("Number is positive.")

# print("I am happy now")

# num = 18
# if (num < 0):
#     print("Number is negative.")
# elif (num > 0):
#     if (num <= 10):
#         print("Number is between 1-10")
#     elif (num > 10 and num <= 20):
#         print("Number is between 11-20")
#     else:
#         print("Number is greater than 20")
# else:
#     print("Number is zero")

import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
timestampH = int(time.strftime('%H'))
print(type(timestampH))
timestampM = time.strftime('%M')
print(timestampM)
timestampS = time.strftime('%S')
print(timestampS)

if (timestampH < 12):
    print("Good Morning, Sir!")
elif (timestampH > 12 and timestampH < 17):
    print("Good Afternoon, Sir!")
elif (timestampH > 17):
    print("Good Eveneing, Sir!")
else:
    print("Hello Sir!")


# https://docs.python.org/3/library/time.html#time.strftime