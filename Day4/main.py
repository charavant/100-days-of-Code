import random
# import my_module

# random_integer = random.randint(0, 1)

# if random_integer == 1:
#     print("Heads")
# else:
#     print("Tails")
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print("dirty_dozen",dirty_dozen)
# print("dirty_dozen[0]",dirty_dozen[0])
# print("dirty_dozen[1]",dirty_dozen[1])
# print("dirty_dozen[1][2]", dirty_dozen[1][2])
# print("dirty_dozen[1][3]",dirty_dozen[1][3])
# print("dirty_dozen[1][1]",dirty_dozen[1][1])

# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇
# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1

# map[number_index][letter_index] = "X"

# line1 = map[0]
# line2 = map[1]
# line3 = map[2]

# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

rps = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(rps[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(rps[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")