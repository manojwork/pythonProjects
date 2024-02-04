import smtplib as sm
import datetime as dt
import random 
my_mail="manojbabu.mandhala@gmail.com"
resever=["1679031manojbabu@gmail.com","manojbabu.mandhala@gmail.com"]
now=dt.datetime.now()
day=now.weekday()
f=open("Qutes.txt","r")
data=f.readlines()
quote=random.choice(data)
f.close()
if day==3:
    with sm.SMTP("smtp.gmail.com",port=587) as connect :
        connect.starttls()
        connect.login(user=my_mail,password="bvydresbbflrglwb")
        connect.sendmail(from_addr=my_mail,to_addrs=resever,msg=f"subject:MONDAY MOTIVATION\n\n {quote} ")
        