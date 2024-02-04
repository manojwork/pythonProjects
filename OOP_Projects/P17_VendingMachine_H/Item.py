class Item:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def __str__(self):
        return " \t"+str(self.name)+" "+str(self.price)+" ("+str(self.quantity)+") "