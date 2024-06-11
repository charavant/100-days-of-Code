# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# # for loop with range
# for number in range(1, 11):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)
   
# # Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
  
# # Write your code below this row 👇

# average_height = sum(student_heights) / len(student_heights)

# print("total height = ",sum(student_heights))
# print("number of students = ",len(student_heights))
# print("average height = ", round(average_height))

# # Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])

# # Write your code below this row 👇
# max = 0
# for score in student_scores:
#     if score > max:
#         max = score
        
# print(f"The highest score in the class is: {max}")

# target = int(input()) # Enter a number between 0 and 1000
# # 🚨 Do not change the code above ☝️

# # Write your code here 👇
# total = 0
# for number in range(0, target + 1):
#     if number % 2 == 0:
#         total += number

# print(total)

# FizzBuzz

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# for letter in range(0, nr_letters):
#     print(random.choice(letters), end="")
# for symbol in range(0, nr_symbols):
#     print(random.choice(symbols), end="")
# for number in range(0, nr_numbers):
#     print(random.choice(numbers), end="")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
for letter in range(0, nr_letters):
    password_list.append(random.choice(letters))
for symbol in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for number in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char  
    
print(f"Your password is: {password}")