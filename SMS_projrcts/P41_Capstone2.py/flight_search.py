from flight_data import FlightData as fd
import requests
from notification_manager import NotificationManager as N
key="W7mL5MR7gMYTsqYk6gj1V-gmNyaLlOGI"
headers = {"apikey": key}
class FlightSearch:
    
    def getIATA(i):
        TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": key}
        query = {"term": i["city"], "location_types": "city"}
        response=requests.get(url=location_endpoint,params=query,headers=headers)
        try:
            code=response.json()['locations'][0]['code']
            fd.putData('iataCode',code,i["id"])
        except:
            print(" No Code .")
        
    def searchExploring(lists):
        for i in lists:
            flight=fd.SearchFlight(i['iataCode'])
            if flight!=None:
                if flight['price']<i['lowestPrice']:
                    temp=f"""  
                             Low Price Alert! Only {round(int(flight['price'])*82.58,3)}Rs/- to fly from Chennai-MAA to {i['city']}-{i['iataCode']} from {flight['outbound_date']} to {flight['inbound_date']} .
                    
                    """
                    N(temp)

        
        