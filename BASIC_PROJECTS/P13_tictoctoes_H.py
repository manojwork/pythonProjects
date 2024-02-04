def display(place):
    for i in range(0,3):
        for j in range(0,3):
            print(place[i][j],end=" ")
        print()

def checking():
    a=int(input(" enter a row : "))
    b=int(input(" enter the spot : "))
    spot=[a,b]
    return spot

def checkwin(place):
    sum=0
    for i in range(3):
        if place[i][i]=="X":
            sum+=1
            if(sum==3):
                print("X won the game .")
                return True
        elif place[i][i]=="O":
            sum-=1
            if(sum==-3):
                print("O won the game .")
                return True
  
    sum=0
    for i in range(3):
        if place[2-i][2-i]=="X":
            sum+=1
            if(sum==3):
                print("X won the game .")
                return True
        elif place[2-i][2-i]=="O":
            sum-=1
            if(sum==-3):
                print("O won the game .")
                return True
   
    sum=0
    for i in range(3):
        for j in range(3):
            if  place[i][j]=="X":
                sum+=1
                if(sum==3):
                    print("X won the game .")
                    return True
            elif place[i][j]=="O":
                sum-=1
                if(sum==-3):
                    print("O won the game .")
                    return True
    
    sum=0
    for i in range(3):
        for j in range(3):
            if  place[j][i]=="X":
                sum+=1
                if(sum==3):
                    print("X won the game .")
                    return True
            elif place[j][i]=="O":
                sum-=1
                if(sum==-3):
                    print("O won the game .")
                    return True
     
    return False   

import random
print("\t\t Tik toc Toes ")
place=[["-","-","-"],["-","-","-"],["-","-","-"]]
j=0
option=""
display(place)
while(j<9):
    if(j%2 == 0):
        print( " Turn X: \n")
        sp=checking()
        place[sp[0]][sp[1]]="X"
        display(place)
        if  checkwin(place) :
            break
    else:
        print(" Turn O: \n")
        sp=checking()
        place[sp[0]][sp[1]]="O"
        display(place)
        if  checkwin(place) :
            break
    j=j+1
