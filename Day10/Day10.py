logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

choice = False

num1 = float(input("What is the first number: "))
print("""
+
-
*
/""")
operation = input("Pick an operation: ")
num2 = float(input("What is the next number: "))

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
answer = operations[operation](num1, num2)

print(f"{num1} {operation} {num2} = {answer}")

continue_cal = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

if continue_cal == "y":
    choice = False
else:
    choice = True
    print("Thank You For Taking Part!!")

while not choice:
    print("""
    +
    -
    *
    /""")
    operation = input("Pick an operation: ")
    num2 = float(input("What is the next number: "))

    num1 = answer
    
    answer = operations[operation](num1, num2)

    print(f"{num1} {operation} {num2} = {answer}")

    continue_cal = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

    if continue_cal == "y":
        choice = False
    else:
        choice = True
        print("Thank You For Taking Part!!")