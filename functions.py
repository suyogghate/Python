# def calculateGmean(a, b):
#     mean = (a*b)/(a+b)
#     print(mean)

# def isGreater(a, b):
#     if(a > b):
#         print("First number is grater!")
#     else:
#         print("Second number is greater!")

# calculateGmean(9, 8)
# isGreater(6, 9)

# def name(fname, mname="Jhon", lname="Whatson"):
#     print("Hello,", fname, mname, lname)

# name("Amy")

# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name(mname = "Peter", lname = "Wesker", fname = "Jade")

# def name(*name):
#     print(type(name))
#     print("Hello,", name[0], name[1], name[2])

# name("James", "Buchanan", "Barnes")

# def name(**name):
#     print(type(name))
#     print("Hello,", name["fname"], name["mname"], name["lname"])

# name(mname = "Buchanan", lname = "Barnes", fname = "James")

# def name(fname, mname, lname):
#     return "Hello, " + fname + " " + mname + " " + lname

# print(name("James", "Buchanan", "Barnes"))

def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)

c = average(5, 6, 7, 1)
print(c)