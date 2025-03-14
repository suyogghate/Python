foods = []
prices = []
total = 0

while True:
    food = input("Enter food to buy (press 'q' to quit): ")
    if food.lower() == "q":
        break;
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("------------YOUR CART-------------")

for food, price in zip(foods, prices):
    print(f"{food} ${price:02}")

for price in prices:
    total += price

print()
print(f"You total bill is: ${total}")