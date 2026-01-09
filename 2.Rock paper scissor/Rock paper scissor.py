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

list = [rock , paper , scissors]
list_of_names = ["rock", "paper", "scissors"]
user_input= int(input("what do you choose?Type 0 for Rock, 1 for Paper, 2 for Scissors:\n"))
print("user chooses:" + list_of_names[user_input] + list[user_input])

comp_input = random.randint(0,2)
print("computer chooses:" + list_of_names[comp_input] + list[comp_input])

if user_input == 0:
    if comp_input == 0:
        print("it's Tie.")
    elif comp_input == 1:
        print("You loose.")
    else:
        print("You win.")
elif user_input == 1:
    if comp_input == 0:
        print("You win.")
    elif comp_input == 1:
        print(" it's Tie.")
    else:
        print("You loose.")
elif user_input == 2:
    if comp_input == 0:
        print("You loose.")
    elif comp_input == 1:
        print("You win.")
    else:
        print("it's Tie.")
else:
    print("Your choice is invalid.")
