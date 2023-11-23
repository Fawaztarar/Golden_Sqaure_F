class Menu:

    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def display(self):
        return "\n".join(f"{dish.name}: ${dish.price}" for dish in self.dishes)

        print(Menu.display())

