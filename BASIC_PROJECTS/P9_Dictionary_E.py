import random
print("\n\n\t Task: 1 \n")
dict={"India":"New Delhi","America":"Washing Turn bc","Sri lanka":"Colombo","Maldives":"Male","Italy":"rome"}
c=list(dict.keys())
score =0
for i in range(3):
    country=random.choice(c)
    guess=input(f" enter the capital of {country} : ")
    if guess == dict[country].lower():
        print(" correct .")
        score+=1
    else:
        print(f" wrong answer   \n {country}: {dict[country]}")
print(f" score : { score }")

print("\n\n\t Task: 2 \n")
sen =input(" enter the str . ")
dic={}
for i in sen:
    dic[i]=dic.get(i,0)+1
for key ,value in dic.items():
    print(f" {key} : {value} ")

