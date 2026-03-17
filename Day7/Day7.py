import random

word_list = ["aardvark", "baboon", "camel"]

word = word_list[random.randint(0,2)]
placeholder = ""
correct_letters = []
game_over = False
lives = 6

print(word)
for letter in word:
    placeholder += "_"
print(placeholder)


while not game_over and lives != 0:
    guess = input("Guess a letter: ")

    display = ""
    
    for letter in word:
        if letter == guess:
            display += guess;
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else: 
            display += "_"
    
    if guess not in word:
        lives -= 1
        print("Guessed letter is wrong. Try Again. ", lives, " left!!")
    
    print(display)
    
    if "_" not in display:
        game_over = True
        print("You Win")
    
    if lives == 0:
        game_over = True
        print("You lost!!")
    

