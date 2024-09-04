import random


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
print(f"Pssst, the correct answer is {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

def number_guessing():
    for attempt in range(attempts):
        print(f"You have {attempts - attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"You got it! The answer was {number}.")
            return
    print("You've run out of guesses, you lose.")
    
replay = True
while replay:
    number_guessing()
    play_again = input("Do you want to play again? Type 'y' or 'n': ")
    if play_again == "n":
        replay = False

print("Goodbye!")