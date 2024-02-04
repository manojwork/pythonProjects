class Airline:
    def __init__(self):
        self.seats=[]
    def getperson(self,i):
        return self.seats[i]
    def setperson(person):
        self.seats[person.seatnumber]=person
    def choosereservation(self,person):
        while person.seatnumber==14:
            person.chooseSeat()
        self.seats.append(person)
        print(f"{person.name} thanks for reserving ")   
        
    def __str__(self):
        temp = ""
        for i in range(len(self.seats)):
           if (self.seats[i] != None):                      
               temp += str(self.seats[i])
               temp += "\n\n";    
           else :
               temp += "Seat " + (i+1) + " is empty."
               temp += "\n\n"
            
        return temp