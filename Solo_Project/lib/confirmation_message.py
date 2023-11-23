from twilio.rest import Client
class TextSender:
    def __init__(self, account_sid, auth_token, from_number):
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number

    def send_text(self, phone, message):
        return self.client.messages.create(
            to=phone,
            from_=self.from_number,
            body=message
        )


class OrderManager():
    def __init__(self, text_sender):
        self.text_sender = text_sender
    
    def place_order(self):
        self.text_sender.send_text("+440000000",
        "Thank you! Your order was placed and will be delivered before 18:52")








# import os
# class ConfimrationText:
    

#     def send_confirmation_text(self, recipient_number, message):
#         account_fawaz = os.environ['AC9b8ac94da892a6bc1adf178985ac8b31']
#         auth_token = os.environ['14a55aee6c39d8107785e3e52eddd63b']
#         twilio_number = os.environ['+447897013182']

#         client = Client(account_sid, auth_token)
#         message = client.messages.create(
#             to= +447599564000,
#             from_=twilio_number,
#             body= "Thank you! Your order was placed and will be delivered before 18:52"
#         )
#         return message.fawaz  # Returns message SID for confirmation


# # order = Order()
# # confirmation_message = "Thank you! Your order was placed and will be delivered before 18:52"
# # order.send_confirmation_text("+447599564000", confirmation_message)