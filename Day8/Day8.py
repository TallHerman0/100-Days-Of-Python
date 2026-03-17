alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
def decrypt(text, shift_amount):
    decrypted_text = ""
    for letter in text:
        if letter in alphabet:  # only shift letters
            new_index = (alphabet.index(letter) - shift_amount) % len(alphabet)
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += letter  # keep symbols unchanged
    print(f"The decoded text is: {decrypted_text}")


def encrypt(original_text, shift_amount):
    coded_word = ""
    for letter in original_text:

        if letter == ' ' or letter not in alphabet:
            coded_word += letter
        else:
            new_index = alphabet.index(letter) + shift_amount
            new_index %= len(alphabet)
            coded_word += alphabet[new_index]
    text = coded_word   
    print(f"Here is the encoded result: {coded_word}")

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
def caeser(direction, text, shift):
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)

choice = "yes"
print(logo)
while choice != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(direction, text, shift)

    choice = input("Type 'yes' if you want to go again. Otherwise, type 'no': ").lower()
    if choice == "no":
        print("")
        print("Goodbye!!")