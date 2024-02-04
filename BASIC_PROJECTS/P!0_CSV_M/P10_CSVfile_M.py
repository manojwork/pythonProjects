import random
import csv
with open("Cars.csv") as f:
    dic=csv.DictReader(f)
    dic_list=list(dic)
dic_brand={}
for i in dic_list:
    dic_brand[i["Make"]]=dic_brand.get(i["Make"],[])+[i["Horsepower"]]

dic_avg={}
for make,hp_list in dic_brand.items():
    hp_sum=0
    for hp in hp_list:
        hp_sum+=int(hp)
    dic_avg[make]=round(hp_sum/len(hp_list),2)
for key,value in dic_avg.items():
    print(f" {key} : {value}")
