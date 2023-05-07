print("Welcome to Pizza store")

size = input("What is your pizza size? S, M, L")
add_pepporini = input("Do you want pepperoni? Y/N")
extra_cheese = input("Do you want extra cheese? Y/N")

amount = 0

if size == "S":
    amount+=15
    if add_pepporini == "Y":
        amount+=2
        if extra_cheese == "Y":
            amount+=3
            print(f"Your final bill is {amount}")
elif size == "M":
    amount+=20
    if add_pepporini == "Y":
        amount+=2
        if extra_cheese == "Y":
            amount+=3
            print(f"Your final bill is {amount}")
elif size == "L":  
    amount+=25  
    if add_pepporini == "Y":
        amount+=2
        if extra_cheese == "Y":
            amount+=3
            print(f"Your final bill is {amount}")
