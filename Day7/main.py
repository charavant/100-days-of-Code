import random
from hangman_words import word_list
from hangman_art import logo, stages
lives = 6
print(logo)

placeholder = ""
chosen_word = random.choice(word_list)
for letter in chosen_word:
    placeholder+= "_"
print(placeholder)    

game_over = False
correct_letters = []
while not game_over:
    print(f"********************************{lives}/6 LIVES LEFT********************************")
    guess = input("Guess a letter: ").lower()
    
    if guess in correct_letters:
        print(f"You have already guessed {guess}")
    
    display = ""
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            
    print(display)
    print(f"word to guess: {chosen_word}")
    
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word")
        
        if lives == 0:
            game_over = True
            
            print(f"***********************It was {chosen_word}... YOU LOSE**********************")
    
    if "_" not in display:
        if display == chosen_word:
            game_over = True
            
            print("********************************YOU WIN********************************")

    print(stages[lives])  

