def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1))

def fibbonacci(num):
    if num < 0:
        print("Incorrect input")
    elif num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibbonacci(num-1) + fibbonacci(num-2)

num = 9
print("Number: ", num)
# print(f"Factorial of {num} : {factorial(num)}")
print(f"Fibbonacci of {num} : {fibbonacci(num)}")