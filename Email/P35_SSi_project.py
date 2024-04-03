import requests
import smtplib as sm
import time
MY_LATITUDE=13.184410
MY_LONGITUDE=80.102058
MAILS=["1679031manojbabu@gmail.com","manojmass421@gmail.com","manojbabu.mandhala@gmail.com"]
MESSAGE=f"subject:Look Up ISS a head..\n\nThe Iss is on the head look up ."
def iss_ahead():
    iss=requests.get("http://api.open-notify.org/iss-now.json")
    iss.raise_for_status()
    data=iss.json()
    ISS_LATITUDE=float(data["iss_position"]["latitude"])
    ISS_LONGITUDE=float(data["iss_position"]["longitude"])
    if MY_LATITUDE+5 >= ISS_LATITUDE>= MY_LATITUDE-5 and MY_LONGITUDE+5>=ISS_LONGITUDE>=MY_LONGITUDE-5:
        return True    

while True:
    time.sleep(30)    
    if iss_ahead():
        with sm.SMTP("smtp.gmail.com",port=587) as connect:
            connect.starttls()
            connect.login(user="manojbabu.mandhala@gmail.com",password="resbbflrglwb")
            connect.sendmail(from_addr="manojbabu.mandhala@gmail.com",to_addrs=MAILS,msg=MESSAGE)
    elif temp==0:
        with sm.SMTP("smtp.gmail.com",port=587) as connect:
            connect.starttls()
            connect.login(user="manojbabu.mandhala@gmail.com",password="bflrglwb")
            connect.sendmail(from_addr="manojbabu.mandhala@gmail.com",to_addrs=MAILS,msg=MESSAGE)
            temp=100
    else:
        temp=200
