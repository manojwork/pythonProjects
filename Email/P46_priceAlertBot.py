import requests 
from bs4 import BeautifulSoup as bs
import xml
import smtplib
link="https://www.amazon.in/Noise-Launched-Bluetooth-Calling-Tracking/dp/B0BJ72WZQ7/ref=sr_1_1?pd_rd_r=53a435c4-860c-4bd1-888e-1726a872db15&pd_rd_w=GWUEz&pd_rd_wg=rpPLJ&pf_rd_p=85e7769d-61b7-4bd0-82bd-ed2d2809eef2&pf_rd_r=QBT2CH3EDDGZSATNZAAM&qid=1687516470&sr=8-1"
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9,te;q=0.8"
}
response=requests.get(link,headers=header)
soup=bs(response.content,"lxml")
price=soup.find("span",class_="a-price-whole").get_text()
prices=price.split(",")
sp=f"{prices[0]}{prices[1]}".split(".")

if int(sp[0])<2000:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connect:
        connect.starttls()
        connect.login(user="manojbabu.mandhala@gmail.com",password="bvydresbbflrglwb")
        connect.sendmail(from_addr="manojbabu.mandhala@gmail.com",to_addrs="manojmass421@gmail.com",msg=f"subject:Price Down alert \n\n The product price down now \n link: {link}")
    