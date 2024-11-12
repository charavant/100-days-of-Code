MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True

def Payment(choice):
    money = 0 
    quarters = input("How many quarters? ")
    dimes = input("How many dimes? ")
    nickels = input("How many nickels? ")
    pennies = input("How many pennies? ")
    if quarters != "":
        money += int(quarters) * 0.25
    if dimes != "":
        money += int(dimes) * 0.10
    if nickels != "":
        money += int(nickels) * 0.05
    if pennies != "":
        money += int(pennies) * 0.01
        
    if (money <= 0):
        
        return 0
    
    if (choice == "espresso"):
        money = money - float(MENU["espresso"]['cost'])
    elif (choice == "latte"):
        money = money - float(MENU["latte"]['cost'])
    else:
        money = money - float(MENU["cappuccino"]['cost'])
    print(f"Money given: {money}")
    return money
   
def PrintReport():
    print(f"water: {resources["water"]}")
    print(f"milk: {resources["milk"]}")
    print(f"coffee: {resources["coffee"]}")
# 1 - print report 2 - check rss sufficient 3 - process coins 4 - Check transaction successful 5 - make coffee

def PrintMenu():
    print(f"Menu:\n espresso: {MENU['espresso']['cost']}$\n latte: {MENU['latte']['cost']}$\n cappuccino: {MENU['cappuccino']['cost']}$")

def CheckRss(choice):
    water = int(resources["water"]) - int(MENU[choice]['ingredients'])
    coffee = int(resources["coffee"]) - int(MENU[choice]['ingredients'])
    bool = (water > 0) and (coffee > 0)
    if choice != "espresso":
        milk = int(resources["milk"]) - int(MENU[choice]['ingredients'])
        bool = bool and (milk > 0)
    return bool

while is_on: 
    PrintMenu()
    choice = input("What would you like?: ")
    if choice == "off":
        is_on = False
        print("Goodbye!")
    elif choice == "report":
        PrintReport()
    else:
        money = Payment(choice)
        if money == 0:
            print("Get out of here!")
            print("\n" * 100)
        elif money >= int(MENU[choice]['cost']):
            enoughRss = CheckRss(choice)
            profit += money
            print(f"Your change is {money - int(MENU[choice]['cost'])}")
