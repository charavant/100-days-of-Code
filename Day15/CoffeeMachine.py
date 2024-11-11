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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def Payment(choice):
    money = 0 
    money += input("How many quarters? ") * 0.25
    money += input("How many Dimes? ") * 0.10
    money += input("How many quarters? ") * 0.05
    money += input("How many quarters? ") * 0.01
    if (choice == "espresso"):
        money = money - MENU["espresso"][1]
    elif (choice == "latte"):
        money = money - MENU["latte"][1]
    else:
        money = money - MENU["cappuccino"][1]
    return money
   
def PrintReport():
    print("water: " + resources["water"])
    print("milk: " + resources["milk"])
    print("coffee: " + resources["coffee"])
# 1 - print report 2 - check rss sufficient 3 - process coins 4 - Check transaction successful 5 - make coffee
