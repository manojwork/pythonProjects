print("\n\t Fictional Car Insurance Comany \n\n")

gender=input(" enter the gender : ")
if gender.lower() == "male":
    age=int(input(" enter the age : "))
    if age<=26:
        tax=23/100
    else:
        tax=9/100
else:
    sport=input(" is your a sport car (yes/no) : ")
    if sport.lower() == "yes":
        tax=21/100
    else:
        tax=10/100
    marketPrice = int(input(" enter the market price of the car : "))
    print(f" Insurance : {round(marketPrice*tax,2)} ")
        

