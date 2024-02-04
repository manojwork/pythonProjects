towers=[[5,4,3,2,1],[],[]]
def move(towers,start,dist):
    towers[dist].append(towers[start].pop())
def display(towers):
    for i in range(5,0,-1):
        for tower in towers:
            if(len(tower)>=i):
                print(tower[i-1],end=" ")
            else:
                print("|",end=" ")
        print()
    print("-----\n\n")
def honai(towers,n,start,dest,mid):
    if(n==0):
        return
    honai(towers,n-1,start,mid,dest)
    move(towers,start,dest)
    display(towers)
    honai(towers,n-1,mid,dest,start)
display(towers)
honai(towers,5,0,2,1)
