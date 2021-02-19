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


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not {item}.")
            return False
        return True


def on_coin_process():
    print("Please insert the coins.")
    total = int(input("Tell the quarters u have? ")) * 0.25
    total += int(input("Tell the dimes u have? ")) * 0.1
    total += int(input("Tell the nickles u have? ")) * 0.05
    total += int(input("Tell the pennies u have? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost)
        print(f"Here is the Rs.{change}, change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("there is no enough money. Returned money")
        return False


def on_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] = order_ingredients[item]
    print(f"Here is your {drink_name}.enjoy")


is_on = True
while is_on:
    choice = input(" What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water:{resources['water']} ml")
        print(f"milk:{resources['milk']} ml")
        print(f"coffee:{resources['coffee']} ml")
        print(f"money: Rs. {profit}")
    else:
        drink_name = MENU[choice]
        if is_resources_sufficient(drink_name["ingredients"]):
            payment = on_coin_process()
            if is_transaction_successful(payment, drink_name['cost']):
                on_coffee(choice, drink_name["ingredients"])

