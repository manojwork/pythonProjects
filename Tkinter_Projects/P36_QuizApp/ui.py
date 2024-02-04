THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import Quiz
class UIDesign:
    def __init__(self,quizz:Quiz):
        self.quiz=quizz
        self.window=Tk()
        self.window.config(padx=15,pady=20,bg=THEME_COLOR)
        self.canvas=Canvas(width=300,height=225,bg="white")
        self.text=self.canvas.create_text(150,125,text=" hello",font=("Arial",16,"bold"),width=290)
        right_image=PhotoImage(file="true.png")
        wrong_image=PhotoImage(file="false.png")
        self.score=0
        self.scoreL=Label(text=f"score: {self.score}",bg=THEME_COLOR,fg="white",font=("Arial",15,"bold"))
        self.right=Button(image=right_image,bg=THEME_COLOR,highlightthickness=0,command=self.corrects)
        self.wrong=Button(image=wrong_image,bg=THEME_COLOR,highlightthickness=0,command=self.wrongs)
        self.gap=Label(text=" ",bg=THEME_COLOR,fg="white",height=2)
        self.grids()
        self.temp=False
        self.ref=None
        self.next_question()
        self.window.mainloop()
        
        
    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has():
            q= self.quiz.nextQuestion()
            self.canvas.itemconfig(self.text,text=q)
        else:
            self.canvas.itemconfig(self.text,text=" No Question")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")
            
            
    def corrects(self):
        self.canvas.config(bg="white")
        if self.quiz.isCorrect("True"):
            self.scoreL.config(text=f"score :{self.quiz.score} ")
            self.temp=True
        else:
            self.temp=False
        self.feeback()
    def wrongs(self):
        if self.quiz.isCorrect("False"):
            self.scoreL.config(text=f"score :{self.quiz.score} ")
            self.temp=True
        else:
            self.temp=False
        self.feeback()
    def feeback(self):
        if self.temp:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.ref=self.window.after(2000,self.next_question)
        
        
    def grids(self):
        self.scoreL.grid(row=0,column=1)
        self.canvas.grid(row=1,column=0,columnspan=2)
        self.gap.grid(row=2,column=0)
        self.right.grid(row=3,column=0)
        self.wrong.grid(row=3,column=1)
        
   