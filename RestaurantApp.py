menu = {
    'Pizza':120,
    'Burger':80,
    'Salad':50,
    'Coffee':35,
    'FREE20':0.2
}

print("Welcome to our Restaurant, Here is our menu: ")
print("\n")
print("Pizza: 120/-\nBurger: 80/-\nSalad: 50/-\nCoffee: 35/-")
print("Apply coupon code FREE20 to get 20% Discount!!!!")

while(True):
    order1 = input("What would you like to have?: ")

    query = input("Do you want to order more?(Yes/No): ")
    if(query == "Yes"):
        print("Pizza: 120/-\nBurger: 80/-\nSalad: 50/-\nCoffee: 35/-")
        print("Apply coupon code FREE20 to get 20% Discount!!!!")
        order2 = input("What would you like to have?: ")
        total_bill = menu[order1]+menu[order2]
        coupon = input("Do you have coupon code, if yes then please enter: ")
        if(coupon == "FREE20"):
            discount_price = total_bill * menu[coupon]
            print("Your bill after 20% Discount: ", total_bill - discount_price)
            break
        else:
            print("Your total bill is: ", menu[order1]+menu[order2])
            break
    elif(query == "No" and order1 == "Coffee"):
        print("Sorry sir, you can't just order coffee!, Please choose again from the menu: ")
        print("Pizza: 120/-\nBurger: 80/-\nSalad: 50/-\nCoffee: 35/-")
        print("Apply coupon code FREE20 to get 20% Discount!!!!")
        order2 = input("What would you like to have?: ")
        total_bill = menu[order1]+menu[order2]
        coupon = input("Do you have coupon code, if yes then please enter: ")
        if(coupon == "FREE20"):
            discount_price = total_bill * menu[coupon]
            print("Your bill after 20% Discount: ", total_bill - discount_price)
            break
        else:
            print("Your total bill is: ", menu[order1]+menu[order2])
            break
    elif(query == "No" and order1 != "Coffee"):
        total_bill = menu[order1]
        coupon = input("Do you have coupon code, if yes then enter it: ")
        if(coupon == "FREE20"):
            discount_price = total_bill * menu[coupon]
            print("Your bill after 20% Discount: ", total_bill - discount_price)
            break
        else:
            print("Your total bill is: ", menu[order1])
            break

print("ThankYou! Visit Again!")