import random


#dice = input("Heads or Tails?")

name_string = input("Give me everybody's name seperated by a comma")
names = name_string.split(", ")

items = len(names)

person = random.randint(0,items -1)
final_name = names[person]


print(f"{final_name} is going to buy meal today")
#Vasya, Petya, Mosya, Kosya, Rvosya