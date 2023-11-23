
from lib.dish import *  

def test_dish_creation():
    dish = Dish("Pizza", 10.99)
    assert dish.name == "Pizza", "Dish name should be 'Pizza'"
    assert dish.price == 10.99, "Dish price should be 10.99"


    