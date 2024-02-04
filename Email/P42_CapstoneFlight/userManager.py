import requests
from flightSearch import FlightSearch as fs
userGet="https://api.sheety.co/886ab59a1c41d29dc87aa5b735b4b037/flights/users"
userPost="https://api.sheety.co/886ab59a1c41d29dc87aa5b735b4b037/flights/users"
userPut="https://api.sheety.co/886ab59a1c41d29dc87aa5b735b4b037/flights/users/"
userDelete="https://api.sheety.co/886ab59a1c41d29dc87aa5b735b4b037/flights/users/"

class User:
   
    def postDetails(fn,sn,username,password,code,email,flyfrom):
        details={
            'user':{
                'firstName':fn,
                'secondName':sn,
                'username':username,
                'password':password,
                'flyfromcode':code,
                'email':email,
                'flyfrom':flyfrom
            }
        }
        posting=requests.post(url=userPost,json=details)
        print(posting.json())
        
    def updateCode(city,code,id):
        details={
            'user':
            {
                'flyfromcode':code,
                'flyfrom':city
            }
        }
        putting=requests.put(url=f"{userPut}/{id}",json=details)
        
    def getUserData():
        response=requests.get(url=userGet)
        return response.json()['users']
     
        
    def verifyUser(username,password):
        response=requests.get(url=userGet)
        data=response.json()
        lists=data['users']
        temp=False
        for i in lists:
            if i['username'] ==username and i['password']==password :
                temp=True
        return temp
        
    def allMails():
        response=requests.get(url=userGet)
        lists= response.json()['users']
        mails=[]
        for i in lists:
            mails.append(i['email'])
        return mails
        