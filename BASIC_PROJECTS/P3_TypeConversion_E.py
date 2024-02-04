print("\n\n\t Task: 1 \n")
a=input(" enter A value : ")
b=input(" enter B value : ")
print(f" {a} * {b} ={int(a)*int(b)} ")

print("\n\n\t Task: 2 \n")
age =int(input(" enter the age : "))
year=2023-age
days=age*365
hours=days*24
minute=hours*60
seconds=minute*60
print(f" year : {year} \n days : {days} \n hours : {hours} \n minutes : {minute} \n seconds : {seconds} ")

print("\n\n\t Task: 3 \n")
price=int(input(" enter the price : "))
per=input(" enter the % of tip : ")
tip=round(price*float(per)/100,2)
print(f" Tip : {tip} ")


