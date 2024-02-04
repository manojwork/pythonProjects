import requests

sheetGet="https://api.sheety.co/886ab59a1c41d29dc87aa5b735b4b037/flights/prices"
sheetPost="https://api.sheety.co/886ab59a1c41d29dc87aa5b735b4b037/flights/prices"
sheetPut="https://api.sheety.co/886ab59a1c41d29dc87aa5b735b4b037/flights/prices/"
sheetDelete="https://api.sheety.co/886ab59a1c41d29dc87aa5b735b4b037/flights/prices/"

class FlightData:
    
    def getPriceData():
        response=requests.get(url=sheetGet)
        return response.json()['prices']
    
    def putPriceData(key,value,id):
        data={
            "price":{
                key:value
            }
        }
        Api=f"{sheetPut}{id}"
        putting=requests.put(url=Api,json=data)
        print(putting.json())
    