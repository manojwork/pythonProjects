from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
BLACK="#000000"
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
  window.after_cancel(timer)
  check.config(text="")
  label.config(text="Timer")
  canvas.itemconfig(text_canvas,text="00:00")
  global rep
  rep=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def starts():
    global rep
    rep+=1
    LONG_BREAK=LONG_BREAK_MIN*60
    SHORT_BREAK=SHORT_BREAK_MIN*60
    WORK=WORK_MIN*60
    if rep%8==0:
        check.config(text=check.cget("text")+"✓")
        label.config(text=" Long Break ")
        countdown(LONG_BREAK)
    elif rep%2==0:
        check.config(text=check.cget("text")+"✓")
        label.config(text=" Short Break ")
        countdown(SHORT_BREAK)
    else:
        label.config(text=" work ")
        countdown(WORK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    canvas.itemconfig(text_canvas,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,countdown,count-1)
    else:
        starts()
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pongarenu")
window.config(padx=100,pady=50,bg="#000000")


label=Label(text="Timer",fg=GREEN,bg=BLACK,font=(FONT_NAME,25,"bold"))
label.grid(column=1,row=0)


canvas=Canvas(width=200,height=224,bg="#000000",highlightthickness=0)
photo=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=photo)
text_canvas=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


start=Button(text="Start",font=(FONT_NAME,10,"bold"),bg=BLACK,highlightthickness=0,fg="white",command=starts)
start.grid(row=2,column=0)


restart=Button(text="Restart",font=(FONT_NAME,10,"bold"),bg=BLACK,highlightthickness=0,fg="white",command=reset)
restart.grid(row=2,column=2)


check=Label(text="",highlightthickness=0,bg=BLACK,fg=GREEN,font=(FONT_NAME,15,"bold"))
check.grid(column=1,row=2)
window.mainloop()