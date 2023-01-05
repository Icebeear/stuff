from data import menu, resources

def commands(answer):
    global state
    if answer == "off":
        state = False
    if answer == "report":
        for key in resources:
            print(f"{key}: {resources[key]}")
        print(cash)
    else: 
        coffe(answer)

def check(order):
    for key in menu[order]["ingredients"]:
        if menu[order]["ingredients"][key] > resources[key]:
            print(f"Sorry, is not enough {key}")
            return 0   

def coffe(order):
    global cash
    cash = 0 
    if check(order) != 0:
        print("Please insert coins")
        cash += int(input("How many quarters?: ")) * 0.25
        cash += int(input("How many dimes?: ")) * 0.1
        cash += int(input("How many nickes?: ")) * 0.05
        cash += int(input("How many pennies?: ")) * 0.01
        price = menu[order]["cost"]
        if cash >= price:
            print(f"Here is ${cash - price} in change.")
            cash -= (cash - price) 
            print(f"Here is your {order} ☕️. Enjoy!")
            for key in resources:
                resources[key] -= menu[order]["ingredients"][key]
        else:
            print("Sorry that's not enough money. Money refunded.")


state = True
while state:
    commands(input("What would you like? (espresso/latte/cappuccino): "))