student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()

#TODO 1. Create a dictionary in this format:
nato = {row.letter:row.code for (index, row) in df.iterrows()}
#print(nato)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
done = False
while not done:
    try:
        name = input("Enter your name: ")
        encrypted = [nato[letter.upper()] for letter in name]
        print(encrypted)
        done = True
    except:
        print("Sorry, only letters in the alphabet please.")

