from lib.dish import * 
from lib.menu import * 



def test_add_dish():
    menu = Menu()
    dish = Dish("Pizza", 10.99)
    menu.add_dish(dish)
    assert dish in menu.dishes, "Dish should be added to the menu"

def test_display_menu():
    menu = Menu()
    dish = Dish("Pizza", 10.99)
    menu.add_dish(dish)
    #print(menu.display())
    expected_output = "Pizza: $10.99"
    
    assert menu.display() == expected_output, "Menu display should show the added dish with its price"


