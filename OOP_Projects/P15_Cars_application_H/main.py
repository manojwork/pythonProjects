from Car import Car
from Dealership import Dealership
cars=[  Car("Nissan", 5000, 2020, "red",["tires", "keys"]),
        Car("Dodge", 8500, 2019, "blue",  ["tires", "keys"]),
        Car("Nissan", 5000, 2017, "yellow",  ["tires", "filter"]),
        Car("Honda", 7000, 2019, "orange", ["tires", "filter"]),
        Car("Mercedes", 12000, 2015, "jet black",  ["tires", "filter", "transmission"])
    ]
deal=Dealership(cars)
print("\n ****** PYTHON DEALERSHIP! ****** \n")
make=input(" Welcome! Enter the type of car you're looking for: ")
budget=input("Enter your budget: ")
if(deal.search(make, budget)):
    print("Thanks for buyying . ")
else:
    print("Feel free to browse through our collection of cars.\n")
    print(deal)
    i=int(input(" enter the index of the car to buy ( start from zero ) : "))
    deal.sellcar(i)
    
 
