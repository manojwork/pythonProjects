from twilio.rest import Client
class NotificationManager:
    def __init__(self,temp):
        self.auth_token="4179eed6370b71165d96531d0396a9a1"
        self.account_sid="ACd9d94ca5223d15da1dc9c4b7d7f3fe6e"
        self.phoneNumber=+13203773105
        self.smssending(temp)
        
    def smssending(self,temp):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
                    .create(
                        body=temp,
                        from_=self.phoneNumber,
                        to='+916281095378'
                    )
    
   


