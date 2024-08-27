alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    encrypted_text = ""
    temp = text.split()
    for word in temp:
        for letter in word:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift
                if new_position > 25:
                    new_position -= 26
                encrypted_text += alphabet[new_position]
            else:
                encrypted_text += letter
    print("encrypted_text: ", encrypted_text)

def decrypt(text, shift):
    decrypted_text = ""
    temp = text.split()
    for word in temp:
        for letter in word:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position - shift
                if new_position < 0:
                    new_position += 26
                decrypted_text += alphabet[new_position]
            else:
                decrypted_text += letter
    print("decrypted_text: ", decrypted_text)

if direction == "encode":
    encrypt(text, shift)  
else:
    decrypt(text, shift)