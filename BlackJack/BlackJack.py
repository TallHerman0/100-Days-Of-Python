import random
from art import logo
import subprocess, os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_cards = []
opp_cards = []

Player = False
Computer = False

def deal_cards(my_list):
    crd = cards[random.randint(0,12)]
    my_list.append(crd)

def sum_of_cards(my_list):
    return sum(my_list)

play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()

if play != 'n':
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

    for number in range(2):
        deal_cards(my_cards)
        deal_cards(opp_cards)

    print(f"Your cards: {my_cards}, current score: {sum_of_cards(my_cards)}")
    print(f"Computer's first card: {opp_cards[0]}")
    
    while not Player or not Computer:
        if 10 and 11 in my_cards:
            Player = True
            if 10 and 11 in opp_cards:
                Player = False
                Computer = True
                break
            break

        play = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if play == 'n':
            while sum_of_cards(opp_cards) < 17:
                deal_cards(opp_cards)
            print(f"Your final hand: {my_cards}, final score: {sum_of_cards(my_cards)}")
            print(f"Computer's final hand: {opp_cards}, final score: {sum_of_cards(opp_cards)}")
            break
        else:
            deal_cards(my_cards)



