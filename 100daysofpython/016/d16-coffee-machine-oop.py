from d16_coffee_maker import CoffeeMaker

coffee_maker = CoffeeMaker()


def start_coffee_machine():
    global coffee_maker
    while coffee_maker.machine_is_on:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        coffee_maker.process_order(order)


start_coffee_machine()
