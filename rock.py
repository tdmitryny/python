import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor."))
game_images[your_choice]

computer_choice = random.randint(0,2)
print(f"Computer's choice is {game_images[computer_choice]}")

if your_choice == 0 and computer_choice == 2:
    print("You win🏆")
    print("Your choice",game_images[your_choice])
elif your_choice == 1 and computer_choice == 2:
    print("you win")
elif computer_choice > your_choice:
    print("Computer wins")
    print("Your choice", game_images[your_choice])
elif computer_choice == your_choice:
    print("It draw")
    print("Your choice",game_images[your_choice])
else:
    print("Please enter right number!")



# num_choice = int(choice[0])
# selected = map[num_choice]
# random_selected = random.randint(0,selected)
# print(random_selected)


