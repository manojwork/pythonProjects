from tkinter import *
from tkinter import messagebox as mb
import random
import json
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
BLACK="#000000"
g=None
#--------------------------PASSWORD GENERATOR-------------------------#
def generator():
    temp=" "
    alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    nums=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    sys=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

    for i in range(6):
        num=random.randint(0,len(alpha)-1)
        temp+=alpha[num]
    for i in range(3):
        n=random.randint(0,9)
        temp+=nums[n]
    for i in range(3):
        n=random.randint(0,len(sys)-1)
        temp+=sys[n]
    tem=[i for i in temp]
    global g
    g="".join(random.sample(tem,len(tem)))
    passentry.delete(0,END)
    passentry.insert(0,g)
#--------------------------PASSWORD GENERATOR-------------------------#
#--------------------------DATA SAVING-------------------------#
def reopen(new_data):
    f=open("passwords.json","w")
    json.dump(new_data,f,indent=4)
    f.close()
def opening(new_data) :
    try:
        f=open("passwords.json","r")
        data=json.load(f)
        data.update(new_data)
        f.close()
        f=open("passwords.json","w")
        json.dump(data,f,indent=4)
        f.close()
    except:
        reopen(new_data)
def adding():
    wed=wedentry.get()
    email=emailentry.get()
    p=passentry.get()
    temp=True
    new_data={
        wed:{
            "email":email,
            "password":p
        }
    }
    
    if len(wed)==0 or len(p)==0 or len(email)==0:
        mb.showerror(title="error",message=" fields are empty ") 
        temp=False
    if temp:
        is_ok=mb.askokcancel(title=" details ",message=f"\n email : {email}\n password : {p} \n wedsite : {wed}")
    if is_ok and temp:
        opening(new_data)
        passentry.delete(0,END)
        wedentry.delete(0,END)   
#--------------------------DATA SAVING-------------------------#
#--------------------------SEARCHING-------------------------#

def searching():
    try :
        f=open("passwords.json","r")
        data=json.load(f)
        f.close()
    except:
          mb.showerror(title=" error ",message=" wedsite not found ! ")
    wedsite=wedentry.get()
    flag=False
    for key,value in data.items():
        if key==wedsite:
            flag=True
            mb.showinfo(title=f"{wedsite}",message=f"\n email : {value['email']} \n password : {value['password']} ")
    if not flag:
        mb.showerror(title=" error ",message=" wedsite not found ! ")
    
        
#--------------------------SEARCHING-------------------------#
#--------------------------UI-------------------------#
window=Tk()
window.title(" password manager ")
window.config(padx=50,pady=50,bg=BLACK)
canvas=Canvas(width=514,height=514,bg=BLACK,highlightthickness=0)
images=PhotoImage(file="password.png")
canvas.create_image(257,257,image=images)
canvas.create_text(257,37,text=" PASSWORD MANAGER ",font=(FONT_NAME,40,"bold"),fill=PINK)


wedLabel=Label(text="Wedsite : ",font=(FONT_NAME,20,"bold"),fg=RED,bg=BLACK)
wedentry=Entry(width=55,bg=BLACK,fg=GREEN)
search=Button(text="Search",width=20,fg=GREEN,bg=BLACK,font=(FONT_NAME,13,"bold"),height=1,command=searching)

emailLabel=Label(text="Email/Username : ",font=(FONT_NAME,20,"bold"),fg=RED,bg=BLACK)
emailentry=Entry(width=100,bg=BLACK,fg=GREEN)
emailentry.insert(0,"manojmass421@gmail.com")

passlabel=Label(text="Password : ",font=(FONT_NAME,20,"bold"),fg=RED,bg=BLACK)
passentry=Entry(width=60,bg=BLACK,fg=YELLOW)

genpass=Button(text="Generate Password ",width=20,fg=GREEN,bg=BLACK,font=(FONT_NAME,13,"bold"),height=1,command=generator)

add=Button(text="Add ",width=20,fg=RED,bg=BLACK,font=(FONT_NAME,13,"bold"),height=1,command=adding)

canvas.grid(row=0,column=1)
wedLabel.grid(row=1,column=0)
wedentry.grid(row=1,column=1)
search.grid(row=1,column=2)
emailLabel.grid(row=2,column=0)
emailentry.grid(row=2,column=1,columnspan=2)
passlabel.grid(row=3,column=0)
passentry.grid(row=3,column=1)
genpass.grid(row=3,column=2)
add.grid(row=4,column=2)
window.mainloop()
#--------------------------UI-------------------------#
