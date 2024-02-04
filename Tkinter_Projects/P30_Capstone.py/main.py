from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
#--------------------data------------------------#
try:
    data=pandas.read_csv("to_learn.csv")
except:
    data=pandas.read_csv("french_words.csv")
info=data.to_dict(orient="records")
to_learn=info
current_card={}
flip=None
def flipcard():
    window.after_cancel(flip)
    canvas.itemconfig(bgimage,image=back_image)
    canvas.itemconfig(title,fill="white",text="English")
    canvas.itemconfig(word,fill="white",text=current_card["English"])
def firstcard():
    global current_card,flip
    current_card=random.choice(to_learn)
    canvas.itemconfig(bgimage,image=front_image)
    canvas.itemconfig(title,fill="black",text="French")
    canvas.itemconfig(word,fill="black",text=current_card["French"])
    flip=window.after(3000,flipcard)
def okclick():
    global to_learn
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv("to_learn.csv",index=False)
    firstcard()
#-------------------UI-----------------------------#
window=Tk()
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_image=PhotoImage(file="D:\Computer Languages\Python Projects\Tkinter_Projects\P30_Capstone.py\images\card_front.png")
back_image=PhotoImage(file="D:\Computer Languages\Python Projects\Tkinter_Projects\P30_Capstone.py\images\card_back.png")

bgimage=canvas.create_image(400,263,image=front_image)
canvas.grid(row=0,column=0,columnspan=2)
title=canvas.create_text(400,150,text="Title",fill="black",font=("Arial",40,"bold"))
word=canvas.create_text(400,263,text="word",fill="black",font=("Arial",30,"italic"))


ok_image=PhotoImage(file="right.png")
wrong_image=PhotoImage(file="wrong.png")
ok_Button=Button(image=ok_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=okclick)
wrong_Button=Button(image=wrong_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=firstcard)
ok_Button.grid(row=1,column=0)
wrong_Button.grid(row=1,column=1)
firstcard()
flip=window.after(3000,flipcard)
window.mainloop()