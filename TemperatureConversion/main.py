unit = input("Is the temperature in Celcius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp} ℉")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celcius is: {temp} ℃")
else:
    print(f"{unit} is not a valid unit of measurement.")