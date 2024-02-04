class Store:
    def __init__(self,lists):
        self.lists=lists
    def despense(self,row,spot):
        if self.lists[row][spot].quantity>0:
            self.lists[row][spot].quantity-=1
            return True
        else:
            return False
    def __str__(self):
        temp=""
        temp+="\t**************************************************************\n"
        temp+="\t                   WELCOME TO PYTHON DRINKS!                  \n"
        temp+="\t**************************************************************\n"
   
        for i in self.lists:
            for j in i:
                temp+=str(j)
            temp+="\n"
        return temp