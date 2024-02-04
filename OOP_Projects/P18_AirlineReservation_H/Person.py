import random
class Person:
    def __init__(self,name,nationality,dateOfBirth,seatnumber):
        self.name=name
        self.nationality=nationality
        self.dateOfBirth=dateOfBirth
        self.seatnumber=seatnumber
        self.passport=[0]
        
    def applypassport(self):
        int=random.randint(0, 1)
        if int==0:
            return False
        else:
            return True
    def chooseSeat(self):
        seat=random.randint(1,13)
        self.seatnumber=seat
    def setpassport(self):
        self.passport=[self.name,self.nationality,self.dateOfBirth,self.seatnumber]
    def __str__(self):
       return " name : "+str(self.name)+" \n"+" nationality : "+str(self.nationality)+" \n Date of birth : "+str(self.dateOfBirth)+" \n passport : "+str(self.passport)+" \n seat number : "+str(self.seatnumber) 
        