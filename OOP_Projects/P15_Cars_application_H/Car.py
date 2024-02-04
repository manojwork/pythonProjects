class Car:
    def __init__(self,make,price,year,colour,parts):
        self.make=make
        self.colour=colour
        self.price=price
        self.parts=parts
        self.year=year
    def getmake(self):
        return str(self.make)
    def getcolour(self):
        return str(self.colour)
    def getprice(self):
        return str(self.price)
    def getparts(self):
        return str(self.parts)
    def setmake(self,make):
        self.make=make
    def setcolour(self,colour):
        self.colour=colour
    def setprice(self,price):
        self.price=price
    def setparts(self,parts):
        self.parts=parts
    def drive(self):
        print("You bought the beautiful " + str(self.year) + " " + self.getcolour()+ " " + self.getmake() + " for " + self.getprice() + ".")
        print("Please drive your car to the nearest exit.\n")
    def __str__(self):
        return " make : "+self.getmake()+" colour : "+self.getcolour()+" price : "+self.getprice()+" parts : "+self.getparts()