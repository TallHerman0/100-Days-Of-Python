MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
drnk = ""
quarters =0; dimes = 0; nickles = 0; pennies = 0
# TODO Prompt to get what the customer wants.

def drinkChoice():
    global drnk
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "espresso":
        drnk = "espresso"
        return MENU["espresso"]
    elif choice == "latte":
        drnk = "latte"
        return MENU["latte"]
    elif choice == "cappuccino":
        drnk = "cappuccino"
        return MENU["cappuccino"]
    elif choice == "report":
        return "report"
    elif choice == "off":
        return "off"

#TODO Create a report fucntion
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${money}")

#TODO Processing of coins
def coin_process(quarts, dims, nicks, penns):
    cost = 0
    cost = (quarts*0.25) + (dims*0.1) + (nicks*0.05) + (penns*0.01)
    return cost

def collect_coins():
    global quarters, nickles, dimes, pennies
    print("Please insert coins")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    penneis = int(input("how many pennies?: "))

def checkResources(drink):
    if "milk" in drink["ingredients"]:
        if (drink["ingredients"]["water"] >= resources["water"]):
            return 1
        elif (drink["ingredients"]["coffee"] >= resources["coffee"]):
            return 2
        elif (drink["ingredients"]["milk"] >= resources["milk"]):
            return 3
        else:
            return 4
    else:
        if (drink["ingredients"]["water"] >= resources["water"]):
            return 1
        elif (drink["ingredients"]["coffee"] >= resources["coffee"]):
            return 2
        else:
            return 4

while 1:
    choice = drinkChoice()
    if choice == "off":
        break
    elif choice == "report":
        report()
        continue 
    else:
        if checkResources(choice) == 1:
            print("Sorry there is not enough water.")
            continue
        elif checkResources(choice) == 2:
            print("Sorry there is not enough coffee.")
            continue
        elif checkResources(choice) == 3: 
            print("Sorry there is not enough milk.")
            continue
        elif checkResources(choice) == 4:
            
            collect_coins()
            paid = coin_process(quarters, dimes, nickles, pennies)
            if paid < choice["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                continue
            if "milk" in choice["ingredients"]:
                resources["water"] -= choice["ingredients"]["water"]
                resources["coffee"] -= choice["ingredients"]["coffee"]
                resources["milk"] -= choice["ingredients"]["milk"]
                money += choice["cost"]
                print(f"Here is ${paid - choice["cost"]} in change.")
                print(f"Here is your {drnk} ☕️. Enjoy!")
            else:
                resources["water"] -= choice["ingredients"]["water"]
                resources["coffee"] -= choice["ingredients"]["coffee"]
                money += choice["cost"]
                print(f"Here is ${paid - choice["cost"]} in change.")
                print(f"Here is your {drnk} ☕️. Enjoy!")
        

