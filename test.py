bill = input("What was the total bill? $")

float_number = float(bill)

ten = 10 / 100
twelve = 12 / 100
fifteen = 15 /100

percentage = input(f"What percentage tip would like to give? 10, 12, or 15?")

total_per = float(percentage) / 100
number_percent  = float_number * total_per


total_number = float_number + number_percent

split = input("How many people to split?")

total = total_number / int(split)


print(f"Each person should pay: ${total // 1}")

