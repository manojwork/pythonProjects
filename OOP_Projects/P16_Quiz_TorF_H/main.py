from QuizBrain import Quiz
from Question import Question
from Data import question_data
question_list=[]

for i in question_data:
    text=i["text"]
    ans=i["answer"]
    question=Question(text, ans)
    question_list.append(question)
    
quiz=Quiz(question_list)
while quiz.stillhave():
    quiz.next_question()
    
print(f"\n\n Total Score {quiz.score}/{len(quiz.question_list)}")
