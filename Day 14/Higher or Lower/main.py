from game_data import data
from art import logo, vs
from random import randint
import os

score = 0
A = randint(0, len(data)-1)
B = randint(0, len(data)-1)
while A == B:
    B = randint(0, len(data)-1)  # Changed to B to avoid reassigning A unnecessarily

def logo_print():
    print(logo)

# Printing the comparisons
def comparisons():
    print(f"Compare A: {data[A]['name']}, a {data[A]['description']}, from {data[A]['country']}")
    print(vs)
    print(f"Compare B: {data[B]['name']}, a {data[B]['description']}, from {data[B]['country']}")

def compare(answer, list, A, B):
    global score
    if (answer == 'A' and list[A]["follower_count"] > list[B]["follower_count"]) or \
       (answer == 'B' and list[B]["follower_count"] > list[A]["follower_count"]):
        score += 1
        return True
    else:
        return False

def game():        
    global A, B
    while True:
        os.system("cls")
        logo_print()
        print(f"You're right! Current score: {score}")
        comparisons()
        answer = input("Who has more followers? 'A' or 'B': ").upper()
        if compare(answer, data, A, B):
            A = B  # Move B to A
            B = randint(0, len(data)-1)
            while A == B:
                B = randint(0, len(data)-1)
        else:
            os.system("cls")
            logo_print()
            print(f"Sorry, that's wrong. Final score: {score}")
            break

game()


