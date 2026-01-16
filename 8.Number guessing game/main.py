import random
import logo

#global declaration
easy_level = 10
hard_level = 5
def check_answer(user_guess,random_number,turns):
    if user_guess == random_number:
        print(f"You got it! The number was {random_number}.")
        return 1
    elif user_guess > random_number:
        print("Too high.")
        return turns -1
    elif user_guess < random_number:
        print("Too low.")
        return turns -1

def difficulty_level():
    choosen_input=input("choose a difficulty. 'easy' or 'hard':")
    if choosen_input == "easy":
        return easy_level
    elif choosen_input == "hard":
        return hard_level

def game():
    print("welcome to the number guessing game!!\n I'm thinking of the number between 1 to 100.")
    print(logo.logo)
    turns = difficulty_level()
    random_number = random.randint(1, 100)

    guess=0
    while guess != random_number:
        print(f"-----you have {turns} turns left-----")
        user_guess = int(input("guess a number between 1 and 100: "))
        turns = check_answer(user_guess,random_number,turns)
        if turns == 0:
            print(f"You run out of the guesses. The number was {random_number}." )
            return
        elif turns == 1:
            print(f"You guessed the number {random_number}.")
            return
        else:
            print("guess again.")

game()