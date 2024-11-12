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

def Payment():
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
    return money
 
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is {change}$")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough mone. Money refunded.")
        return False
  
def PrintReport():
    print(f"water: {resources["water"]}")
    print(f"milk: {resources["milk"]}")
    print(f"coffee: {resources["coffee"]}")

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")    

def PrintMenu():
    print(f"Menu:\n espresso: {MENU['espresso']['cost']}$\n latte: {MENU['latte']['cost']}$\n cappuccino: {MENU['cappuccino']['cost']}$")

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True    
    
while is_on: 
    PrintMenu()
    choice = input("What would you like?: ")
    if choice == "off":
        is_on = False
        print("Goodbye!")
    elif choice == "report":
        PrintReport()
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            money = Payment()
            if is_transaction_successful(money, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
            