class Dealership:
    def __init__(self,cars):
        self.cars=[]
        for i in cars:
            self.cars.append(i)
    def setcar(self,car):
        self.cars.append(car)
    def getcar(self,i):
        return self.cars[i]
    def sellcar(self,i):
        self.cars[i].drive()
        return self.cars.pop(i)
    def search(self,name,dubget):
        for i in self.cars:
            if i.getmake().lower()==name and i.getprice()<=dubget:
                print(" finded \n\t are you interested y/n. ")
                n=input("")
                if n=="y":
                    self.sellcar(self.cars.index(i))
                    return True
        return False
    def __str__(self):
        temp=""
        for i in self.cars:
            temp+=str(i)+"\n"
        return temp