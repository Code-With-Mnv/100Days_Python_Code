# Author : Manav
# Task : Coffee Machine Program

resources = {"milk": 5000, "water": 5000, "coffee": 1000}
espresso = {"water": 30, "coffee": 15, "price": 1.5}
latte = {"milk": 50, "water": 30, "coffee": 15, "price": 2.0}
cappuccino = {"milk": 100, "water": 60, "coffee": 30, "price": 3.0}
coffee_choice = input("Which coffee would you like to have (espresso/latte/cappuccino): ")


def enough_rsrc(coffee_choice):
    if coffee_choice.lower() == "espresso":
        if resources["water"] >= espresso["water"] and resources["coffee"] >= espresso["coffee"]:
            return True
        else:
            return False

    elif coffee_choice.lower() == "latte":
        if (resources["milk"] >= latte["milk"] and resources["water"] >= latte["water"]
                and resources["coffee"] >= latte["coffee"]):
            return True
        else:
            return False

    elif coffee_choice.lower() == "cappuccino":
        if (resources["milk"] >= cappuccino["milk"] and resources["water"] >= cappuccino["water"]
                and resources["coffee"] >= cappuccino["coffee"]):
            return True
        else:
            return False

    else:
        return False


def make_coffee(coffee_choice):
    can_be_made = enough_rsrc(coffee_choice)
    if can_be_made:

        print(f"Your {coffee_choice} is being prepared!")

        if coffee_choice.lower() == "espresso":
            resources["water"] -= espresso["water"]
            resources["coffee"] -= espresso["coffee"]
            print(f"Your EsPresso costs {espresso["price"]}$")

        elif coffee_choice.lower() == "latte":
            resources["milk"] -= latte["milk"]
            resources["water"] -= latte["water"]
            resources["coffee"] -= latte["coffee"]
            print(f"Your Latte costs {latte["price"]}$")

        elif coffee_choice.lower() == "cappuccino":
            resources["milk"] -= cappuccino["milk"]
            resources["water"] -= cappuccino["water"]
            resources["coffee"] -= cappuccino["coffee"]
            print(f"Your Cappuccino costs {cappuccino["price"]}$")

        else:
            print("Errr! Machine ran into a problem!")
            print("Returning you money!")

        money_manage(coffee_choice)

    else:
        print("Sorry! Not enough resources for this coffee. Try another one!")


def money_manage(coffee_choice):
    one_cent = int(input("One Cent Coins: "))
    five_cent = int(input("Five Cent Coins: "))
    ten_cent = int(input("Ten Cent Coins: "))
    fifty_cent = int(input("Fifty Cent Coins: "))
    total_sum = (0.01 * one_cent) + (0.05 * five_cent) + (0.10 * ten_cent) + (0.50 * fifty_cent)
    if coffee_choice.lower() == "espresso":
        price = espresso["price"]
    elif coffee_choice.lower() == "latte":
        price = latte["price"]
    else:
        price = cappuccino["price"]

    if is_price_paid(coffee_choice, total_sum):
        change = total_sum - price
        print("Here is your hot and steamy coffee!")
        print("Here is your change: ", change)
    else:
        print("Price not paid! Coffee will not be served!")


def is_price_paid(coffee_choice, total_sum):
    if coffee_choice.lower() == "espresso" and total_sum >= espresso["price"]:
        return True
    elif coffee_choice.lower() == "latte" and total_sum >= latte["price"]:
        return True
    elif coffee_choice.lower() == "cappuccino" and total_sum >= cappuccino["price"]:
        return True
    else:
        return False


def resource_report():
    print(f"Milk: {resources["milk"]} ML")
    print(f"Water: {resources["water"]} ML")
    print(f"Coffee: {resources["coffee"]} ML")


while True:
    make_coffee(coffee_choice)
    print()
    resource_report()
    break
