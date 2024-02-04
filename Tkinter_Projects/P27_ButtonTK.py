import tkinter as Tk
window=Tk.Tk()
window.title(" kms to miles convertor ")
window.minsize(300,200)
label=Tk.Label(text="  hello welcome ! ",font=("Arial",15,"bold"))
label1=Tk.Label(text=" Kms : ",font=("Arial",10,"bold"))
entry=Tk.Entry(text=" enter the kms ",width=20)

def display():
    km=entry.get()
    miles=int(km)*0.621371
    label2.config(text=f"{round(miles,3)} miles")
button=Tk.Button(text=" calculate ",font=("Arial",12,"bold"),command=display)
label2=Tk.Label(text="none",font=("Arial",12,"bold"))
label.place(x=70,y=0)
label1.place(x=20,y=50)
entry.place(x=70,y=50)
button.place(x=200,y=40)
label2.place(x=100,y=130)
window.mainloop()