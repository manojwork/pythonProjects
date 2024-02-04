from Item import Item
from Store import Store    
store=[[],[],[]]    
store[0].append(Item("Pepsi", 1.99, 3))
store[0].append(Item("Fresca", 1.49, 3))
store[0].append(Item("Brisk", 2.49, 2))
store[1].append(Item("Fanta", 1.99, 2))
store[1].append(Item("Barq's", 1.49, 2))
store[1].append(Item("A & W", 2.49, 3))
store[2].append(Item("Crush", 1.99, 2))
store[2].append(Item("C-Cola", 1.49, 2))
store[2].append(Item("Berry", 2.49, 1))
shop=Store(store)
option="yes"
while option.lower()=="yes":
    print(shop)
    row=int(input("\t enter the row of the drink : "))
    spot=int(input(f"\t enter the spot of the drink in the {row} row : "))
    if shop.despense(row, spot):
        option=input("\n\t thanks for buyying do you want to  buy another (yes/no): ")
    else :
        option=input(" the drink is out of stock do you want to duy another (yes/no): ")