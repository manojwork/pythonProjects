class Quiz:
    def __init__(self,listq):
        self.question_num=0
        self.question_list=listq
        self.score=0
        
    
    def next_question(self):
        currect_question=self.question_list[self.question_num]
        self.question_num+=1
        user_answer=input(f"\n\nQ{self.question_num}: {currect_question.question} (True/False) : ")
        self.checksq(user_answer,currect_question.answer)
        
    def checksq(self,user,ans):
        if user.lower()==ans.lower():
            self.score+=1
            print(" is correct . ")
        else:
            print(" its wrong . ")
        print(f" answer : {ans}")
        print(f" Score : {self.score}/{self.question_num}")
        
    def stillhave(self):
        return self.question_num<len(self.question_list)
        
        