import requests
import datetime as dt

PIXEL_API="https://pixe.la/v1/users"
PROFILE_PAGE="https://pixe.la/@manojbabu"

data={
    "token":"1dhcbu3e37redv272ebs",
    "username":"manojbabu",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"  
}

post_response=requests.post(url=PIXEL_API,json=data)# user account creation

Header={
    "X-USER-TOKEN":"1dhcbu3e37redv272ebs"
}

graph_config={
    "id":"manoj123",
    "name":"Coding Habit Tracking",
    "unit":"hours",
    "type":"float",
    "color":"ichou"
}

Graph_Api=f"{PIXEL_API}/{data['username']}/graphs"

graph_creation=requests.post(url=Graph_Api,json=graph_config,headers=Header)# graph creation 
print(Graph_Api)

posting_api=f"{Graph_Api}/{graph_config['id']}"
now=dt.datetime.now()
posting_data={
    "date":now.strftime("20%y%m%d"),
    "quantity":str(input(" enter how many hours you did programming : "))   
}

posting=requests.post(url=posting_api,json=posting_data,headers=Header)# posting value pixel to the graph
print(posting.text)

def putMethod(): # updating the pixel
    print(posting_api)
    PUT_APi=f"{posting_api}/20{posting_data['date']}"
    put_data={
        "quantity":str(input(" enter the data to put : "))
    }
    putting=requests.put(url=PUT_APi,json=put_data,headers=Header)
    print(putting.text)
    
def deleteMethod(): # deleting the pixel
    DELETE_APi=f"{posting_api}/20{posting_data['date']}"
    deleteing=requests.put(url=DELETE_APi,headers=Header)
    print(deleteing.text)