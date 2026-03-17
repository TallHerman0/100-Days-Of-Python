import subprocess, os

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
#subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

print(logo)

choice = False

auction = {}

while choice != True:
    name = input("What is your name: ")
    bid = int(input("What's your bid: R"))
    bidder = input("Is there another bidder(y/n): ").lower()

    auction[name] = bid

    if bidder == "n":
        choice = True
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    else:
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

highest_amount = 0
highest_bidder = ""
for key in auction:
    if highest_amount < auction[key]:
        highest_bidder = key
        highest_amount = auction[key]

print(f"The winning bidder is {highest_bidder} with R{highest_amount}")
