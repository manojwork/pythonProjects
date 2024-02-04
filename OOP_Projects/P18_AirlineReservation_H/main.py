from Person import Person
from Airline import Airline
people=[]
people.append(Person("Cleopatra", "Egypt", "69 BC", 14))
people.append(Person("Alexander the Great", "Macedon", "356 BC", 14))
people.append(Person("Julius Caesar", "Rome", "100 BC", 14))
people.append(Person("Hannibal", "Carthage", "247 BC", 14))
people.append(Person("Confucius", "China", "551 BC", 14))
people.append(Person("Pericles", "Greece", "429 BC", 14))
people.append(Person("Spartacus", "Thrace", "111 BC", 14))
people.append(Person("Marcus Aurelius", "Rome", "121 AD", 14))
people.append(Person("Leonidas", "Greece", "540 BC", 14))
people.append(Person("Sun Tzu", "China", "544 BC", 14))
people.append(Person("Hammurabi", "Babylon", "1750 BC", 14))
air=Airline()
for i in people:
    if i.applypassport()==True:
        air.choosereservation(i)
        i.setpassport()
        
print("********************** RESERVATIONS COMPLETE! **********************\n")
print(air)

