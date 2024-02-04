import html
from question_model import Question
class Quiz:
    def __init__(self,question):
        self.question_number=0
        self.score=0
        self.questions_list=question
        self.current_question =None
    def still_has(self):
        return self.question_number<len(self.questions_list)
    def nextQuestion(self):
        self.current_question=self.questions_list[self.question_number]
        self.question_number+=1
        q=html.unescape(self.current_question.Question)
        return f" {self.question_number} : {q}"
    def isCorrect(self,user_answer):
        answer=self.current_question.answer
        if  answer.lower()==user_answer.lower():
            self.score+=1
            return True
        else:
            return False
        
        