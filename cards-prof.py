# This program implements the card class
# It reads in a sequence of cards from a file (one card per line)
# and returns a the list sorted by rank and suit.



class Card:
    def __init__ (self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    rankd = {1: "Ace", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 
             6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten",
             10:"Ten", 11:"Jack", 12:"Queen",13:"King"}

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def __str__(self):
        return self.rankd[self.rank] + " of " + self.suit

def use_rank(card):
    return card.getRank()

def use_suit(card):
    return card.getSuit()


def main():
    cardlist = []
    ranktointd = {"Jack":11, "Queen":12, "King":13, "Ace":1, "2":2,
                     "3":3, "4":4, "5":5, "6":6, "7":7, "8":8,
                     "9":9,"10":10}
    infile = open("cards_new.txt", "r")
    for line in infile:
         temp = line.split()
         card = Card(ranktointd[temp[0]], temp[1].rstrip())
         cardlist.append(card)
    cardlist.sort(key=use_rank)
    cardlist.sort(key=use_suit)
    for i in cardlist:
         print(i)
        
main()
