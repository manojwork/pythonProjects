import random
print("  1:Rock 2:Paper 3:Scissor ")
u=int(input(" enter the number (1-3) : "))
c=random.randint(1, 3)
if u == 1:
    if c == 2:
        print(f" Computer won  {c} ")
    else:
        print(" you won ")
elif u == 2:
    if c == 3:
        print(f" Computer won  {c} ")
    else:
        print(" you won ")
elif u==3:
    if c == 1:
        print(f" Computer won  {c} ")
    else:
        print(" you won ")