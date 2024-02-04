class Movie:
    def __init__(self,name,direct,rating):
        self.name=name
        self.direct=direct
        self.rating=rating
        self.availability=True
        self.rentalstatus=False
    def __str__(self):
        if(self.direct == "BlueRay"):
            return "   "+str(self.rating)+"       "+self.direct+"       "+self.name
        return "   "+str(self.rating)+"       "+self.direct+"           "+self.name
    def setavailability(self,j):
        self.availability=j
    def getavailability(self):
        return self.availability
    def setrating(self,i):
        self.rating=i
    def getrating(self):
        return self.rating
    def getname(self):
        return self.name


class MovieStore:
    def __init__(self):
        self.movies=[]
        self.rent=[]
    def add_movie(self,movie):
        self.movies.append(movie)
        movie.setavailability(True)     
    def pop_movie(self,i):
        return self.movies.pop(i)
    def __str__(self):
        temp=" "
        temp+="\t********************************MOVIE STORE*******************************"
        for i in self.movies:
            temp+="\n\t"+str(i)+"\n"
        temp+="\t**************************************************************************"
        return temp
    def getmovie(self,i):
        return self.movies[i]
    def getrentalmovie(self,i):
        return self.rent[i]
    def add_rent(self,n):
        self.rent.append(n)
        self.rentalstatus=True
    def pop_rent(self,i):
        return self.rent.pop(i)
        self.rentalstatus=False
    def __len__(self):
        return len(self.movies)
    def len(self):
        return len(self.rent)
    def strrent(self):
        temp=" "
        temp+="\t********************************MOVIE STORE*******************************"
        for i in self.rent:
            temp+="\n\t"+str(i)+"\n"
        temp+="\t**************************************************************************"
        return temp



store=MovieStore()
store.add_movie( Movie("The Shawshank Redemption", "BlueRay", 9.2))
store.add_movie( Movie("The Godfather", "BlueRay", 9.1))
store.add_movie( Movie("The Godfather: Part II", "DVD", 9.0))
store.add_movie( Movie("The Dark Knight", "BlueRay", 9.0))
store.add_movie( Movie("Schindler's List", "DVD", 8.9))
store.add_movie( Movie("The Lord of the Rings: The Return of the King", "BlueRay", 8.9))
store.add_movie( Movie("Pulp Fiction", "DVD", 8.8))
store.add_movie( Movie("The Good, the Bad and the Ugly", "DVD", 8.8))
store.add_movie( Movie("The Shawshank Redemption", "BlueRay", 9.2))
print(store)
def buymovie():
    buy=int(input(" enter the index of the movie to buy : "))
    if store.getmovie(buy).getavailability()== True:
        store.pop_movie(buy)
        print(" Successfully")
    else:
        print(" the movie was not there . ")

def rentalmovie():
    rental=int(input(" enter the index of the movie for rental : "))
    if store.getmovie(rental).getavailability()==True:
        store.add_rent(store.pop_movie(rental))
        print(" Successfully")
    else:
        print(" the movie was not there . ")
def returning_movie():
    print(store.strrent())
    name=input(" enter the name of the movie which you want to return : ")
    for i in range(store.len()):
        if name.lower() == store.getrentalmovie(i).getname().lower():
            store.add_movie(store.pop_rent(i))
            t=True
    if t == True:
        print(" Successfully")
    else:
        print(" the movie was not there . ")
def add_movie():
    name=input(" enter the name of the movie : ")
    direct=input(" enter the play mode of the movie : ")
    rating=float(input(" enter the rating of the movie : "))
    if(rating<0):
        print("INVALID INPUT ")
        return
    store.add_movie(Movie(name,direct,rating))
    for i in range(len(store)):
        if name.lower() == store.getmovie(i).getname().lower():
            if store.getmovie(i).getavailability == True:
                print(" successfully")
def rating():
    i=int(input(" enter the index of the movie to rate : "))
    rating=float(input(" enter the rating of the movie : "))
    if(rating<0):
        print("INVALID INPUT ")
        return
    if( i<0):
        print("INVALID INPUT ")
        return

    store.getmovie(i).setrating(rating)
    print("successfully")

def switch(n):
    if n=='a':
        buymovie()
    elif n=='b':
        rentalmovie()
    elif n=='c':
        returning_movie()
    elif n=='d':
        rating()
    elif n=='e':
        add_movie()

               


while True:
    n=input("\n\ta).to buy movie\n\tb).to take rental movie \n\tc).to return movie\n\td).to rate a movie\n\te).to add a movie\n\tenter your option : ")
    switch(n)
    print(store)