from art import logo
import random

ANSWER = random.randint(1,100)
lives = 0
win = False

def check_number(num):
    global lives
    global win

    if lives != 0:
        if num > ANSWER:
            print("Too High")
            lives -= 1
        elif num < ANSWER:
            print("Too Low")
            lives -= 1
        elif num == ANSWER:
            print(f"You got it!! The answer was {num}")
            win = True
    else:
        print("You've run out of guesses. Refresh the page to run again.")

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5

print(f"You have {lives} attempts remaining to guess the number.")

while not win:
    Guess = int(input("Make a guess: "))
    check_number(Guess)
    if win:
        break
    if lives != 0:
        print("Guess again.")
        print(f"You have {lives} attempts remaining to guess the number.")
    else:
        print("You've run out of guesses. Refresh the page to run again.")
        break
