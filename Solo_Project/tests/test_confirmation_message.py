
from lib.dish import * 
from lib.menu import * 
from lib.order import * 
from lib.confirmation_message import OrderManager
from unittest.mock import Mock

def test_place_order():
    # Create a mock TextSender
    mock_text_sender = Mock()
    mock_text_sender.send_text.return_value = 'MockMessageSent'

    # Initialize OrderManager with the mocked TextSender
    order_manager = OrderManager(mock_text_sender)

    # Call place_order
    order_manager.place_order()

    # Assert that send_text was called correctly
    mock_text_sender.send_text.assert_called_once_with(
        "+440000000",
        "Thank you! Your order was placed and will be delivered before 18:52"
    )

    print("Test passed!")








    # text_sender = Mock()
    # text_sender.send_text.return_value = true

    # order_manager = OrderManager()
    # order_manager.send_text(text_sender)






# from twilio.rest import Client



# import os

# account_sid = os.getenv('TWILIO_ACCOUNT_SID')
# auth_token = os.getenv('TWILIO_AUTH_TOKEN')
# client = Client(account_sid, auth_token)


# twilio_number = 'your_twilio_phone_number'
# recipient_number = 'recipient_phone_number'
# message_body = 'Hello from Twilio!'

# message = client.messages.create(
#     to=recipient_number,
#     from_=twilio_number,
#     body=message_body
# )

# print(message.sid)



# try:
#     message = client.messages.create(
#         to=recipient_number,
#         from_=twilio_number,
#         body=message_body
#     )
#     print(message.sid)
# except Exception as e:
#     print(f"An error occurred: {e}")