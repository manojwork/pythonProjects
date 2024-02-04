from flight_data import FlightData as fd
from flight_search import FlightSearch as fs
from pprint import pprint

data=fd.getData()
Lists=data["prices"]
def IATACODE():
    for i in Lists:
        if i['iataCode']=="":
            fs.getIATA(i)
IATACODE()
fs.searchExploring(Lists)