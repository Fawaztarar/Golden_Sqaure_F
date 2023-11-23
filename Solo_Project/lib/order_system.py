# import twilio 
# import datetime



# class OrderSystem:
#     def __init__(self, account_sid, auth_token, from_phone_number):
#         self.client = Client(account_sid, auth_token)
#         self.from_phone_number = from_phone_number

#     def place_order(self, customer_phone_number, order_details):
#         # Process the order...
#         delivery_time = datetime.datetime.now() + datetime.timedelta(hours=1)
#         delivery_time_str = delivery_time.strftime("%H:%M")
#         self.send_confirmation_text(customer_phone_number, delivery_time_str)

#     def send_confirmation_text(self, to_phone_number, delivery_time):
#         message_body = f"Thank you! Your order was placed and will be delivered before {delivery_time}"
#         message = self.client.messages.create
# 
#             (to=to_phone_number,
#             from_=self.from_phone_number,
#             body=message_body)
#             return message.sid