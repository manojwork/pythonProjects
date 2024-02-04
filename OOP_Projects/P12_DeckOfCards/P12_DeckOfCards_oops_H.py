import random
class Card:
    suits =['\u2666', '\u2665', '\u2663', '\u2660']
    ranks =["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    
    def __str__(self):
        return f"{Card.ranks[self.rank]}{Card.suits[self.suit]}"
    def __lt__(self,other):
        if self.rank==other.rank:
            return self.suit<other.suit
        else:
            return self.rank<other.rank
class Deck():
    def __init__(self):
        self.deck=[]
        for i in range(4):
            for j in range(13):
                self.deck.append(Card(i,j))
        deck=random.shuffle(self.deck)
            
    def __len__(self):
        return len(self.deck)
    def add_Card(self,card):
        self.deck.append(card)
    def pop_Card(self):
        return self.deck.pop()
class Hand(Deck):
    def __init__(self,label):
        self.deck=[]
        self.label=label
        self.win_Count=0
    def __str__(self):
        temp=""
        temp+=self.label+" : "
        for i in self.deck:
            temp+=str(i)
        return temp
    def get_Label(self):
        return self.label
    def round_Winner(self):
        self.win_Count+=1
    def get_Win_Count(self):
       return self.win_Count

decks=Deck()
hands=[]
for i in range(1,5):
    hands.append(Hand(f"P{i}"))
while(len(decks)>0):
    for hand in hands:
        hand.deck.append(decks.pop_Card())
for i in range(13):
    play=[]
    for hand in hands:
        play.append(hand.pop_Card())
    winner=max(play)
    winner_name=hands[play.index(winner)]
    winner_name.round_Winner()
    print(f"R{i} : { [str(i) for i in play]}",end=" ")
    print(f" winner = {winner_name.get_Label()} {winner}")
for hand in hands:
    print(hand.get_Win_Count())