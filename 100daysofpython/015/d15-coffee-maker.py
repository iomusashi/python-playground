from d15_coffee_maker_data import MENU
from d15_coffee_maker_data import resources
from d15_coffee_maker_data import unit_measurement

# Order Commands
TURN_OFF_COMMAND = "off"
REPORT_COMMAND = "report"
ESPRESSO_ORDER = "espresso"
LATTE_ORDER = "latte"
CAPPUCCINO_ORDER = "cappuccino"

# Global state variables
money_earnings = 0.0
machine_is_on = True


def report():
    for key in resources:
        print(f"{key}: {resources[key]}{unit_measurement[key]}")
    print(f"Money: ${money_earnings}")


def process_order(order: str):
    if order == TURN_OFF_COMMAND:
        stop_coffee_machine()
    elif order == REPORT_COMMAND:
        report()
    elif order in [ESPRESSO_ORDER, LATTE_ORDER, CAPPUCCINO_ORDER]:
        print(f"{order} is being processed")
        initiate_order(order)
    else:
        print("Input cannot be understood. Please try again.")


def initiate_order(order: str):
    if are_resources_sufficient(order):
        process_coins(order)
    else:
        report_exhausted_resources(order)


def process_coins(order: str):
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? "))
    inserted_sum_total = sum_of_coins(quarters, dimes, nickles, pennies)
    if is_coin_sufficient(order, inserted_sum_total):
        change = calculate_change(order, inserted_sum_total)
        serve_change(change)
        profit = inserted_sum_total - change
        add_earnings(profit)
        make_coffee(order)
    else:
        report_insufficient_coins(inserted_sum_total)


def sum_of_coins(quarters: float,
                 dimes: float,
                 nickles: float,
                 pennies: float) -> float:
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01


def is_coin_sufficient(order: str,
                       inserted_coin_value: float) -> float:
    return inserted_coin_value >= MENU[order]["cost"]


def report_insufficient_coins(coin_value: float):
    print(f"Sorry that's not enough money. ${inserted_sum_total} refunded.")


def add_earnings(profit: float):
    global money_earnings
    money_earnings += profit


def serve_change(change: float):
    print(f"Here is $%.2f dollars in change." % change)


def make_coffee(order: str):
    resources["water"] -= MENU[order]["ingredients"]["water"]
    resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
    if order != ESPRESSO_ORDER:
        resources["milk"] -= MENU[order]["ingredients"]["milk"]
    serve_coffee(order)


def serve_coffee(order: str):
    print(f"Here is your {order.lower()}. Enjoy!")


def calculate_change(order: str, inserted_coin_value: float) -> float:
    return inserted_coin_value - MENU[order]["cost"]


def are_resources_sufficient(order: str) -> bool:
    is_water_sufficient = resources["water"] >= MENU[order]["ingredients"]["water"]
    is_coffee_sufficient = resources["coffee"] >= MENU[order]["ingredients"]["coffee"]
    if order == ESPRESSO_ORDER:
        return is_water_sufficient and is_coffee_sufficient
    else:
        is_milk_sufficient = resources["milk"] >= MENU[order]["ingredients"]["milk"]
        return is_water_sufficient and is_coffee_sufficient and is_milk_sufficient


def report_exhausted_resources(order: str):
    for ingredient in MENU[order]["ingredients"]:
        if resources[ingredient] < MENU[order]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}")


def start_coffee_machine():
    global machine_is_on
    while machine_is_on:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        process_order(order)


def stop_coffee_machine():
    global machine_is_on
    machine_is_on = False


start_coffee_machine()
