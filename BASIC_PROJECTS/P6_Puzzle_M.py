import random
print("\n\n\t Task: 1 \n")
words =["father","enterprise","science","programming","resistance","fiction","condition","reverse",
"computer","python"]
word=random.choice(words)
t=[i for i in word ]
g="".join(random.sample(t,len(t)))
print(f" {g} ")
guess=input("guess the word : ")
if guess==word:



    
    print(" you won ")
else :
    print (f" word = {word}\n you lost ")

print("\n\n\t Task: 2 \n")
list=[i if i%2 == 0 else i*i for i in range(10)]
text=input(" text : ")
dic={i:text.count(i) for i in text}
print(list)
print(dic)

