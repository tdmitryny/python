year = int(input("What year you want to check?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
           print("Leap year")
        else:
            print("Not a Leap year")
    else:
     print("Leap year")
else:
    print("Not a leap") 