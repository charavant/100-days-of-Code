from art import logo
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

def calculator():
    print(logo)
    continue_calculating = True
    num1 = float(input("What's the first number?: "))

    while continue_calculating:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}") 
        user_response = input("Type 'y' to continue calculating or 'n' to exit: ").lower()
        if user_response == "n":
            continue_calculating = False
            print("\n * 20")
            calculator()
        else:
            num1 = answer



calculator()
  