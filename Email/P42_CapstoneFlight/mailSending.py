import smtplib as sm
import random
my_mail="manojbabu.mandhala@gmail.com"
password="bvlrglwb"
connect=sm.SMTP("smtp.gmail.com",port=587)
connect.starttls()
connect.login(user=my_mail,password=password)
num=[1,2,3,4,5,6,7,8,9,0]

def otp(mail):
    connect=sm.SMTP("smtp.gmail.com",port=587)
    connect.starttls()
    connect.login(user=my_mail,password=password)
    temp=" Your OTP for Magic's Flight Club : "
    number=""
    for i in range(4):
        n=random.choice(num)
        number+=str(n)
        temp+=str(n)
            
    connect.sendmail(from_addr=my_mail,to_addrs=mail,msg=f"subject:Magic's Flight Club OTP \n\n{temp}")
    connect.close()
    return str(number)

def sendmails(temp,mails):
    connect=sm.SMTP("smtp.gmail.com",port=587)
    connect.starttls()
    connect.login(user=my_mail,password=password)
    connect.sendmail(from_addr=my_mail,to_addrs=mails,msg=f"subject:Magic's Flight Club Deals \n\n{temp}")
    connect.close()