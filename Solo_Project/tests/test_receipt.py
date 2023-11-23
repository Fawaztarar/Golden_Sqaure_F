

# from lib.dish import * 
# from lib.menu import * 
# from lib.order import * 
# import unittest

# import io
# import unittest.mock

# # Set up
# order = Order()
# dish1 = Dish("Pizza", 10)
# dish2 = Dish("Pasta", 8)
# order.add_to_order(dish1, 2)
# order.add_to_order(dish2, 3)

# # Test receipt total
# assert order.calculate_total() == 44, "Total calculation is incorrect"

# # Test generate receipt
# #expected_receipt = "2x Pizza - $10 each\n3x Pasta - $8 each\nTotal: $44\n"

# expected_receipt = "2x Pizza - $10 each\n3x Pasta - $8 each\nTotal: $44\n\n"
# with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
#     order.generate_receipt()
#     assert mock_stdout.getvalue() == expected_receipt, "Receipt generation is incorrect"

















# class TestReceipt(unittest.TestCase):
#     def setUp(self):
#         self.order = Order()
#         self.dish1 = Dish("Pizza", 10)
#         self.dish2 = Dish("Pasta", 8)
#         self.order.add_to_order(self.dish1, 2)
#         self.order.add_to_order(self.dish2, 3)

#     def test_receipt_total(self):
#         self.assertEqual(self.order.calculate_total(), 44)







    # def test_generate_receipt(self):
    #     expected_receipt = "2x Pizza - $10 each\n3x Pasta - $8 each\nTotal: $44\n"
    #     with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
    #         self.order.generate_receipt()
    #         self.assertEqual(mock_stdout.getvalue(), expected_receipt)