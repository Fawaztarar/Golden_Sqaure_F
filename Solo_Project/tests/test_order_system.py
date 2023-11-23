# from unittest.mock import Mock, patch
# from lib.order_system import OrderSystem  # Replace with your actual module

# @patch('your_order_module.Client')
# def test_send_confirmation_text(mock_client):
#     # Set up mock Twilio client
#     mock_message = Mock()
#     mock_message.sid = "SM123456"
#     mock_client.return_value.messages.create.return_value = mock_message

#     # Initialize the OrderSystem with mock credentials
#     system = OrderSystem("dummy_sid", "dummy_token", "+1234567890")

#     # Call the method
#     sid = system.send_confirmation_text("+0987654321", "18:52")

#     # Assertions
#     assert mock_client.return_value.messages.create.called, "Twilio client's create method was not called"
#     assert sid == "SM123456", "SID returned from send_confirmation_text does not match expected value"

# # Run the test
# test_send_confirmation_text()