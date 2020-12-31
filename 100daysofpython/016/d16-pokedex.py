from prettytable import PrettyTable

table = PrettyTable()


def set_field_names():
    global table
    table.field_names = ["Pókemon Name", "Type"]


def setup_data():
    global table
    table.add_row(["Pikachu", "⚡️ Electric"])
    table.add_row(["Charmander", "🔥Fire"])
    table.add_row(["Squirtle", "💧Water"])
    table.add_row(["Bulbasaur", "🍃Grass"])


def set_alignment():
    global table
    table.align["Pókemon Name"] = "r"
    table.align["Type"] = "l"


set_field_names()
setup_data()
set_alignment()
print(table)
