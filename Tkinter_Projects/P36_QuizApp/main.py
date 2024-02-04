from ui import UIDesign
from question_model import Question
from data import Questions
from quiz_brain import Quiz
Questions_list=[]
for question in Questions:
    q=question["question"]
    a=question["correct_answer"]
    Questions_list.append(Question(question=q,answer=a))
quizz=Quiz(Questions_list)
design=UIDesign(quizz)
