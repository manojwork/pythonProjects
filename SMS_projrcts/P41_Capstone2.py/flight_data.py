import requests
import datetime as dt
sheetGet="https://api.sheety.co/297806ab476aa88c32d77c267997fc2a/flights/prices"
sheetPost="https://api.sheety.co/297806ab476aa88c32d77c267997fc2a/flights/prices"
sheetPut="https://api.sheety.co/297806ab476aa88c32d77c267997fc2a/flights/prices/"
sheetDelete="https://api.sheety.co/297806ab476aa88c32d77c267997fc2a/flights/prices/"
now=dt.datetime.now()
datef=dt.datetime(now.year,now.month,now.day+1)
datet=datef+dt.timedelta(days=6*30)
class FlightData:
        

    def getData():
        response=requests.get(url=sheetGet)
        return response.json()
    def putData(key,value,id):
        data={
            "price":{
                key:value
            }
        }
        Api=f"{sheetPut}{id}"
        putting=requests.put(url=Api,json=data)
        print(putting.json())
    
    def SearchFlight(flyto):
        key="W7mL5MR7gMYTsqYk6gj1V-gmNyaLlOGI"
        TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
        headers = {"apikey": key}
        fly_from="MAA"
        
        datefrom=datef.strftime("%d/%m/20%y")
        dateto=datet.strftime("%d/%m/20%y")
        query = {
            "fly_from": fly_from,
            "fly_to": flyto,
            "date_from": datefrom,
            "date_to":dateto,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )
        try: 
            response.json()['data'][0]['price']
        except:
            return None
        flight={
                            "price":response.json()['data'][0]['price'],
                            "dep_city_name":response.json()['data'][0]['cityFrom'],
                            "dep_airport_code":response.json()['data'][0]['cityCodeFrom'],
                            " arrial_city":response.json()['data'][0]['cityTo'],
                            "arrial_city_code":response.json()['data'][0]['cityCodeTo'],
                            "outbound_date":response.json()['data'][0]["route"][0]["local_departure"].split("T")[0],
                            "inbound_date":response.json()['data'][0]["route"][1]["local_departure"].split("T")[0]
                        }
        return flight