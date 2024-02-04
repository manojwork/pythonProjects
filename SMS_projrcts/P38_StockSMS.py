import requests
import datetime as dt
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
key="3H3RIX9UDTEWYL6H"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything?q=tesla%20inc&apiKey=fcf652a0d4924c408c72762862c39b4a"

URL=f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK_NAME}&interval=60min&apikey={key}"

def yesterdayData(data):
    today=dt.datetime.now()
    yesterday_day=today.day-1
    return checkDAta(data,today,yesterday_day)

def dayAfterYesterdayData(data):
    today=dt.datetime.now()
    dayAfyesterday_day=today.day-2
    return checkDAta(data,today,dayAfyesterday_day)
    
def checkDAta(data,today,yesterday_day):
    yesterdayclose=None
    while True:
        try:
            yesterday=dt.datetime(today.year,today.month,yesterday_day)
            data['Time Series (60min)'][f"{yesterday.year}-0{yesterday.month}-0{yesterday.day} 19:00:00"]
        except KeyError:
            yesterday_day-=1
        else:
            break
    if yesterday.month<10 and  yesterday.day<10:
        yesterdayclose=data['Time Series (60min)'][f"{yesterday.year}-0{yesterday.month}-0{yesterday.day} 19:00:00"]["4. close"]
    elif yesterday.day<10:
        yesterdayclose=data['Time Series (60min)'][f"{yesterday.year}-{yesterday.month}-0{yesterday.day} 19:00:00"]["4. close"]
    elif yesterday._month<10:
            yesterdayclose=data['Time Series (60min)'][f"{yesterday.year}-0{yesterday.month}-{yesterday.day} 19:00:00"]["4. close"]
    else:
            yesterdayclose=data['Time Series (60min)'][f"{yesterday.year}-{yesterday.month}-{yesterday.day} 19:00:00"]["4. close"]
    return yesterdayclose
def sms(temp):
    auth_token="4179eed6370b71165d96531d0396a9a1"
    account_sid="ACd9d94ca5223d15da1dc9c4b7d7f3fe6e"
    phoneNumber=+13203773105
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                    body=temp,
                    from_=phoneNumber,
                    to='+916281095378'
                )
                    
def smsSending(PERDIFF):
    if PERDIFF>=5:
        news_response=requests.get(url=NEWS_ENDPOINT)
        news=news_response.json()
        TOP_Three=news["articles"][:3]
        for n in TOP_Three:
            headline=n["title"]
            brief=n["description"]
            temp=f"""TSLA: 🔺2%
            Headline: {headline} (TSLA)?. 
            Brief: {brief}"""
            sms(temp)
                            
                        
response=requests.get(URL)
data=response.json()
yesterday_close=float(yesterdayData(data))
dayAfyesterday_close=float(dayAfterYesterdayData(data))
differance=abs(float(yesterday_close)-float(dayAfyesterday_close))
PERDIFF=(differance/dayAfyesterday_close)*100
smsSending(PERDIFF)
