from art import logo, vs
from game_data import data
import random

#GENERATE A RANDOM PERSON
def generate_person():
    return random.choice(data)

#COMPARE TWO PEOPLE
def compare(person1, person2):
    print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}.")
    print(vs)
    print(f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}.")
    

#CHECK IF THE GUESS IS CORRECT
def check_guess(person1, person2, guess):
    if person1['follower_count'] > person2['follower_count']:
        return guess == 'a'
    else:
        return guess == 'b'

#MAIN FUNCTION
def higher_lower_game():
    print(logo)
    score = 0
    person1 = generate_person()
    person2 = generate_person()
    
    while True:
        compare(person1, person2)
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if check_guess(person1, person2, guess):
            score += 1
            print(f"You're right! Current score: {score}.")
            person1 = person2
            person2 = generate_person()
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break

bool = True
while bool:
    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if play_again == 'n':
        bool = False
    else:
        higher_lower_game()