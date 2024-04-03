import random
import smtplib as sm
import pandas
import datetime as dt
# bday letter set up
def letterfun():
    with open("letter_1.txt","r") as f1:
        file1=f1.read()
    with open("letter_2.txt","r") as f2:
        file2=f2.read()
    with open("letter_3.txt","r") as f3:
        file3=f3.read()
    letters=[file1,file2,file3]
    letter=random.choice(letters)
    return letter
def sendingmail(mail,letter):
    with sm.SMTP("smtp.gmail.com",port=587) as connect:
        connect.starttls()
        connect.login(user="manojbabu.mandhala@gmail.com",password="bvydrrglwb")
        connect.sendmail(from_addr="manojbabu.mandhala@gmail.com",to_addrs=mail,msg=f"subject:Happy Birthday\n\n {letter}")
#finding the Bday person.
data=pandas.read_csv("birthdays.csv")
for index,row in data.iterrows():
    date_of_birth=dt.datetime(row.year,row.month,row.day)
    now=dt.datetime.now()
    if now.day == date_of_birth.day and now.month == date_of_birth.month:
        letter=letterfun()
        letter=letter.replace("[NAME]",row.Name)
        letter=letter.replace("Angela","Manoj")
        sendingmail(row.email,letter)
        
        
        
