from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError("Name cannot be empty string or white space!")

    def add_food(self, food_type: str, name: str, price: float):
        if food_type == 'Bread':
            x = Bread(name, price)

        elif food_type == 'Cake':
            x = Cake(name, price)

        else:
            return

        for el in self.food_menu:
            if el.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")

        self.food_menu.append(x)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand:str):
        if drink_type == 'Water':
            x = Water(name, portion, brand)

        elif drink_type == 'Tea':
            x = Tea(name, portion, brand)

        else:
            return

        for el in self.drinks_menu:
            if el.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        self.drinks_menu.append(x)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type == 'InsideTable':
            x = InsideTable(table_number, capacity)
        elif table_type == 'OutsideTable':
            x = OutsideTable(table_number, capacity)
        else:
            return

        for el in self.tables_repository:
            if el.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        self.tables_repository.append(x)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for el in self.tables_repository:
            if number_of_people <= el.capacity:
                if not el.is_reserved:
                    el.reserve()
                    return f"Table {el.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        ordered = ''
        not_ordered = ''
        res = ''
        table = [x for x in self.tables_repository if x.table_number == table_number]
        if table:
            table = table[0]
            for f in food_names:
                food = [x for x in self.food_menu if x.name == f]
                if food:
                    food = food[0]
                    table.order_food(food)
                    ordered += f' - {food.name}: {food.portion}g - {food.price}lv\n'
                else:
                    not_ordered += f + '\n'
            res += f'Table {table_number} ordered:\n'
            res += ordered
            res += f'{self.name} does not have in the menu:\n'
            res += not_ordered
            return res[:-1]
        else:
            return f"Could not find table {table_number}"

    def order_drink(self, table_number: int, *drinks_names):
        ordered = ''
        not_ordered = ''
        res = ''
        table = [x for x in self.tables_repository if x.table_number == table_number]
        if table:
            table = table[0]
            for f in drinks_names:
                drink = [x for x in self.drinks_menu if x.name == f]
                if drink:
                    drink = drink[0]
                    table.order_food(drink)
                    ordered += f' - {drink.name}: {drink.portion}g - {drink.price}lv\n'
                else:
                    not_ordered += f + '\n'
            res += f'Table {table_number} ordered:\n'
            res += ordered
            res += f'{self.name} does not have in the menu:\n'
            res += not_ordered
            return res[:-1]
        else:
            return f"Could not find table {table_number}"

    def leave_table(self, table_number: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                bill = table.get_bill()
                return f'''Table: {table_number}"
"Bill: {bill:.2f}'''

    def get_free_tables_info(self):
        res = ''
        for table in self.tables_repository:
            res += table.free_table_info() + '\n'

    def get_total_income(self):
        income = 0
        for table in self.tables_repository:
            income += table.get_bill()
        return f"Total income: {income:.2f}lv"