word_list = ["aardvark", "baboon", "camel"]
import random

placeholder = ""
chosen_word = random.choice(word_list)
for letter in chosen_word:
    placeholder+= "_"
print(placeholder)    

#TODO-1: Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

bool = False
while not bool:
    guess = input("Guess a letter: ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
        else:
            display += "_"
    print(display)
    if display == chosen_word:
        bool = True
        print("You win")

