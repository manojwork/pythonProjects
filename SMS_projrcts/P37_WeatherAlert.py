import requests
from twilio.rest import Client
MY_LATITUDE=13.184410
MY_LONGITUDE=80.102058
APICALL=f"https://api.openweathermap.org/data/2.5/forecast?lat={MY_LATITUDE}&lon={MY_LONGITUDE}&appid=b1d89d812eb9bd070f881431ad976a56"
response=requests.get(url=APICALL)
data=response.json()
hoursly=data["list"][:12]
temp=False
for whether in hoursly:
    if whether["weather"][0]["id"]<700:
        temp=True
        
if temp:
    auth_token="4179eed6370b71165d96531d0396a9a1"
    account_sid="ACd9d94ca5223d15da1dc9c4b7d7f3fe6e"
    phoneNumber=+13203773105
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="Rain Alert ! today its going to be rain please carry umbrella .",
                        from_=phoneNumber,
                        to='+916281095378'
                    )