from d16_coffee_maker_comparable_meta import ComparableEnum
from d16_coffee_maker_menu import Menu
from d16_coffee_maker_money_machine import MoneyMachine

from enum import Enum, EnumMeta


class CoffeeMaker:
    """
    Models the machine that makes the coffee,
    and turns it on by default
    """

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.menu = Menu()
        self.money_machine = MoneyMachine()
        self.machine_is_on = True

    def process_order(self, order: str):
        """Accept an order string an process it for commands"""
        if order not in CoffeeMakerCommands:
            print("Input cannot be understood. Please try again.")
            return
        command = CoffeeMakerCommands(order)
        if command == CoffeeMakerCommands.TURN_OFF:
            self.__turn_off_machine()
        elif command == CoffeeMakerCommands.REPORT:
            self.__report()
        elif command.value in self.menu:
            print(f"{command.value} is being processed")
            self.__initiate_order(order)
        else:
            print("Input cannot be understood. Please try again.")
            return

    def __initiate_order(self, order):
        """
        Attempt to fulfill the order if resources are sufficient
        """
        if self.__is_resource_sufficient(order):
            self.__process_coins(order)

    def __process_coins(self, order):
        """
        Attempt to fulfill order if payment is sufficient
        """
        cost = self.menu.cost_of_drink(order)
        if cost == 0.0:
            print("Cannot calculate cost of order, as order not found in menu")
            return
        is_paid = self.money_machine.make_payment(cost)
        if is_paid:
            self.__make_coffee(order)

    def __is_resource_sufficient(self, order):
        """
        Returns True when order can be made,
        False if ingredients are insufficient.
        """
        can_make = True
        drink = self.menu.find_drink(order)
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def __make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        drink = self.menu.find_drink(order)
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        print(f"Here is your {drink.name} ☕️. Enjoy!")

    def __turn_off_machine(self):
        """Turns off the coffee maker object"""
        self.machine_is_on = False

    def __report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")


class CoffeeMakerCommands(Enum, metaclass=ComparableEnum):
    TURN_OFF = "off"
    REPORT = "report"
    ESPRESSO = "espresso"
    LATTE = "latte"
    CAPPUCCINO = "cappuccino"
