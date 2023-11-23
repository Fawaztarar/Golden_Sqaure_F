class Order:
    def __init__(self):
        self.items = {}

    def add_to_order(self, dish, quantity):
        self.items[dish] = self.items.get(dish, 0) + quantity

    def calculate_total(self):
        return sum(dish.price * quantity for dish, quantity in self.items.items())

    def generate_receipt(self):
        receipt = "Itemized Receipt:\n"
        for dish, quantity in self.items.items():
            receipt += f"{quantity}x {dish.name} - ${dish.price} each\n"
        receipt += f"Grand Total: ${self.calculate_total()}\n"
        return receipt






















    # def __init__(self):
    #     self.selections = {}

    # def add_to_order(self, dish, quantity):
    #     self.selections[dish] = quantity

    # def calculate_total(self):
    #     return sum(dish.price * quantity for dish, quantity in self.selections.items())

    # def generate_receipt(self):
    #     for dish, quantity in self.selections.items():
    #         print(f"{quantity}x {dish.name} - £{dish.price} each")
    #     print(f"Total: £{self.calculate_total()}")