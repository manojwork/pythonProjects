import datetime as dt 
import requests
import flightData as fd 
import json

key="W7mL5MR7gMYTsqYk6gj1V-gmNyaLlOGI"
headers = {"apikey": key}
now=dt.datetime.now()
datef=dt.datetime(now.year,now.month,now.day+1)
datet=datef+dt.timedelta(days=6*30)
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
datefrom=datef.strftime("%d/%m/20%y")
dateto=datet.strftime("%d/%m/20%y")
lists=[]
class FlightSearch:
    
    def message(items):
        temp="\n\n Low Price Alert!\n\n"
        for i in items:
            temp+=f" * {i['dep_city_name']} To {i['arrial_city'] } in {round(int(i['price'])*82.58,3)}Rs/-  {i['outbound_date']} - {i['inbound_date']} \n "
        return temp
    
    def getIATA(i):
        query = {"term": i["city"], "location_types": "city"}
        response=requests.get(url=location_endpoint,params=query,headers=headers)
        try:
            code=response.json()['locations'][0]['code']
            fd.FlightData.putPriceData('iataCode',code,i["id"])
        except:
            fd.FlightData.putPriceData('iataCode','NONE',i["id"])
        
    def searchExploring(lis,fly_from):
        for i in lis:
            flight=FlightSearch.__SearchFlight__(i['iataCode'],fly_from,i['id'])
        sortedList=sorted(lists,key=lambda x:x["price"])
        Items=sortedList[:5]
        return FlightSearch.message(Items)
        
                    
    def __SearchFlight__(flyto,fly_from,id):
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
        global lists
        try: 
            price=response.json()['data'][0]['price']
            lists.append({ "price":price,
                        "dep_city_name":response.json()['data'][0]['cityFrom'],
                        "dep_airport_code":response.json()['data'][0]['cityCodeFrom'],
                        "arrial_city":response.json()['data'][0]['cityTo'],
                        "arrial_city_code":response.json()['data'][0]['cityCodeTo'],
                        "outbound_date":response.json()['data'][0]["route"][0]["local_departure"].split("T")[0],
                        "inbound_date":response.json()['data'][0]["route"][1]["local_departure"].split("T")[0]
                        })
        except:
            price=99999
        
    def getIATAForUser(city):
            query = {"term":city, "location_types": "city"}
            response=requests.get(url=location_endpoint,params=query,headers=headers)
            try:
                code=response.json()['locations'][0]['code']
                return code
            except:
                return "Noting"
            
            