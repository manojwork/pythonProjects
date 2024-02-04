import requests
import datetime as dt
data=None
today=dt.datetime.now()
todayDate=today.strftime("20%y%m%d")
todayTime=today.strftime("%H:%M:%S")
d=None
def excercise():
    API_KEY="4850315872e2b563fd9ff105087780d0"
    APP_ID="b2e9aeab"
    API="https://trackapi.nutritionix.com/v2/natural/exercise"
    Header={
        "x-app-id":APP_ID,
        "x-app-key":API_KEY
    }
    Body={
        "query":input(" what you did today :"),
        "gender":"Male",
        "height_cm":"167",
        "age":"20"
    }
    post_request=requests.post(url=API,json=Body,headers=Header)
    global data
    data=post_request.json()
    
def postSheetData():
    POST_API="https://api.sheety.co/297806ab476aa88c32d77c267997fc2a/workouts/workouts"
    Bodys={
      "workout": { 
        "date":todayDate,
        "time":todayTime,
        "exercise":data['exercises'][0]['user_input'],
        "duration":data['exercises'][0]['duration_min'],
        "calories":data['exercises'][0]['nf_calories']}
    }
    posting=requests.post(url=POST_API,json=Bodys)
    posting.raise_for_status()
    global d
    d=posting.json()
    print(posting.text)
    
def putSheetData():
    PUT_API=f"https://api.sheety.co/297806ab476aa88c32d77c267997fc2a/workouts/workouts/{d['workout']['id']}"
    excercise()
    Bod={
      "workout": { 
        "date":todayDate,
        "time":todayTime,
        "exercise":data['exercises'][0]['user_input'],
        "duration":data['exercises'][0]['duration_min'],
        "calories":data['exercises'][0]['nf_calories']}
    }
    putting=requests.put(url=PUT_API,json=Bod)
    putting.raise_for_status()
    print(putting.text)

def deleteRecord():
    DELETE_API=f"https://api.sheety.co/297806ab476aa88c32d77c267997fc2a/workouts/workouts/{d['workout']['id']}"
    deleteing=requests.put(url=DELETE_API)
    deleteing.raise_for_status()
    print(deleteing.text)
    
excercise()
postSheetData()
putSheetData()