#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-2: What happens if the user enters a number/symbol/space?

def caesar(text, shift, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
                shift *= -1
    for letter in text:
        if letter in alphabet:
            new_position = alphabet.index(letter) + shift
            new_position %= len(alphabet)
            output_text += alphabet[new_position]
        else:
            output_text += letter
    print(f"{encode_or_decode}d text: {output_text}")
    
#TODO-3: Can you figure out a way to ask the user if they want to restart the cipher program?

restart = True
while restart:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text, shift, direction)
    
    restart_input = input("Do you want to restart the program? Type 'yes' or 'no':\n").lower()
    if restart_input == "no":
        restart = False
        print("Goodbye!")
    elif restart_input == "yes":
        print("Restarting program...")
    else:
        print("Invalid input. Exiting program.")


