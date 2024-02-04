from flightData import FlightData as fd
from flightSearch import FlightSearch as fs
from userManager import User as u
import mailSending as mail
print(" Hello Welcome to the Magic's Flight Club BOT ")
input()
print(" -Here you can find the best deals of the flights between 6 months of time")
print("1.Login")
print("2.Register")
username=""
member=""
cityData=fd.getPriceData()
while True:
    try:
        key=int(input("enter the option (1/2) : "))
        if key not in [1,2]:
            print(" ﴾͡๏̯͡๏﴿ O'RLY? invalid input the option should 1 or 2 .\n please enter again .")
        else:
            break 
    except:
        print(" ﴾͡๏̯͡๏﴿ O'RLY? invalid input the option should 1 or 2 .\n please enter again .")
if key==1:
    data=u.getUserData()
    print("\n\n\n_________Login Page_________\n")
    while True:
        
        username=input(" User Name :- ")
        password=input(" Password :- ")
        if u.verifyUser(username,password):
            print("\n\n (づ｡◕‿‿◕｡)づ Verifed .....")
            break
        else:
            print("\n\n ﴾͡๏̯͡๏﴿ O'RLY? Verification failed please enter again ...")
    for i in data:
        if username==i['username']:
            member=i
    code=''
    nativeInfo=input("\n ◉_◉  Do you want to Change Your Native \n type (yes/no) : ")
    if nativeInfo in "YESyes":
        while True :
            native=input(" enter the Native (eg:Chennai,Goa,...) :-")
            code=fs.getIATAForUser(native)
            if code=="Noting":
                print( "\n\n ლ(ಠ益ಠლ) Invaid City \n retype \nHint:- City is to be Capital of State (or) it must contain an  well developed airport .")
            else:
                print(" ʕ•ᴥ•ʔ verified ....\n")
                u.updateCode(native,code,member['id'])
                print(" ̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿  Updated...")
                break
        temp=fs.searchExploring(cityData,code)
        mail.sendmails(temp,member['email'])
    else:
        temp=fs.searchExploring(cityData,i['flyfromcode'])
        mail.sendmails(temp,member['email'])
else:
    print("\n\n\n_________Registration Page_________\n")
    firstname=input(" first name : ")
    secondname=input(" last name : ")
    while True :
            native=input(" Native (eg:Chennai,Goa,...) :-")
            code=fs.getIATAForUser(native)
            if code=="Noting": 
                print( "\n\n ლ(ಠ益ಠლ) Invaid City \n retype \nHint:- City is to be Capital of State (or) it must contain an  well developed airport .")
            else:
                print("\n ʕ•ᴥ•ʔ verified ....\n")
                break
    email1=input(" email : ")
    confirmMail=input(" confirm email : ")
    while email1 !=confirmMail:
        print(" not matching enter again .")
        email1=input(" email : ")
        confirmMail=input(" confirm email : ")
    otpnum=mail.otp(confirmMail)
    entered=str(input(" enter the otp : "))
    while otpnum!=entered:
        entered=input(" invalid enter again : ")
    username=input(" username : ")
    data=u.getUserData()
    flag=False
    while True:
        for i in data:
            if i['username']==username:
                flag=True
        if flag:
            username=input(" already used enter another : ")
            flag=False
        else:
            break
    password=input("\n password : ")
    while len(password)<8:
        password=input("\n password  Must be More than 8 items : ")
    u.postDetails(firstname,secondname,username,password,code,confirmMail,native)
    temp=fs.searchExploring(cityData,code)
    mail.sendmails(temp,confirmMail)
        
    
        
    
    
        
    
    

            
        
    
    
