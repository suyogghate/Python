import random

print("Welcome to Snake, Water, Gun game: ")
choice = True

while choice:
    print("Comp's choosing...")
    randomNum = random.randint(1, 3)

    if randomNum == 1:
        comp = 'S'
    elif randomNum == 2:
        comp = 'W'
    elif randomNum == 3:
        comp = 'G'

    def playGame(comp, you):
        if comp == you:
            print("Game tied!!")
        elif comp=='S':
            if you=='W':
                print(f"Comp chose snake({comp}) and you chose water({you}), you lose!")
            elif you=='G':    
                print(f"Comp chose snake({comp}) and you chose gun({you}), you won!") 
        elif comp=='W':
            if you=='G':
                print(f"Comp chose water({comp}) and you chose gun({you}), you lose!")
            elif you=='S':    
                print(f"Comp chose water({comp}) and you chose snake({you}), you won!")
        elif comp=='G':
            if you=='S':
                print(f"Comp chose gun({comp}) and you chose snake({you}), you lose!")
            elif you=='W':
                print(f"Comp chose gun({comp}) and you chose water({you}), you won!")

    you = input("Enter your choice (Snake(S)/Water(W)/Gun(G)): ")
    playGame(comp, you)

    n = input("Do you want to play agin?(Y/N): ")
    if n == 'Y':
        choice = True
    else:
        choice = False

print("Thank you for participating!!")