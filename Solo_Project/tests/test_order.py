
from lib.dish import * 
from lib.menu import * 
from lib.order import * 





def test_add_to_order():
    order = Order()
    dish = Dish("Pizza", 10)
    order.add_to_order(dish, 2)
    assert dish in order.items, "Dish should be added to the order"
    assert order.items[dish] == 2, "Quantity of dish in order should be 2"



def test_calculate_total():
    order = Order()
    dish1 = Dish("Pizza", 10)
    dish2 = Dish("Pasta", 15)
    order.add_to_order(dish1, 2) # 20
    order.add_to_order(dish2, 1) # 15
    total = order.calculate_total()
    assert total == 35, "Total should be 35"



def test_generate_receipt():
    # Creating an order and adding items
    order = Order()
    pizza = Dish("Pizza", 10)
    pasta = Dish("Pasta", 12)
    order.add_to_order(pizza, 2)
    order.add_to_order(pasta, 1)

    # Generating the expected receipt
    expected_receipt = (
        "Itemized Receipt:\n"
        "2x Pizza - $10 each\n"
        "1x Pasta - $12 each\n"
        "Grand Total: $32\n"
    )
    #print(order.generate_receipt())    # fail the pytest
    

    # Asserting the generated receipt against the expected one
    assert order.generate_receipt() == expected_receipt, "Receipt generation failed"