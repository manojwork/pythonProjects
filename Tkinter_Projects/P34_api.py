from  tkinter import *
import requests
#=-----------
def quote():
    api=requests.get(url="https://api.kanye.rest")
    api.raise_for_status()
    data=api.json()
    q=data["quote"]
    canvas.itemconfig(a,text=q)
#---------UI-------#
window=Tk()
window.config(padx=15,pady=15)
canvas=Canvas(width=300,height=414)
bg=PhotoImage(file="background.png")
head=PhotoImage(file="kanye.png")
canvas.create_image(150,207,image=bg)
a=canvas.create_text(150,207,text=" ",width=250,font=("Arial",20,"bold"),fill="white")
canvas.grid(row=0,column=0)
button=Button(image=head,command=quote)
button.grid(row=1,column=0)
window.mainloop() 