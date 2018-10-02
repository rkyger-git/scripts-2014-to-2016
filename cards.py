# file: cards.py
# A program that takes a list of cards, creates card objects, and prints out
# the cards grouped by suit and in rank order within suit.

class Card:

    def __init__(self,rank,suit):

        self.rank = rank
        self.suit = suit

        self.rankdict = {1:"Ace", 2:"Two", 3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Jack", 12:"Queen", 13:"King"}
        self.suitdict = {"c":"Clubs", "d":"Diamonds", "h":"Hearts", "s":"Spades"} 
                

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def __str__(self):
        return self.rankdict[self.rank] + " of " + self.suitdict[self.suit]


def main():
    print("This program takes a list of cards, creates card objects, and prints out\n"
            "the cards grouped by suit and in rank order within suit.\n")

    infile = open("cards_new.txt", "r")

    # use list comprehension to make list of lists from infile
    cardlist = [line.split(" ") for line in infile]
    
    # remove \n from cardlist
    cardlist = [[i[0],i[1].rstrip()] for i in cardlist]
        
    clrankdict = {"Ace":1, "2":2, "3":3, "4":4, "5":5,"6":6,"7":7, "8":8,"9":9,"10":10, "Jack":11, "Queen":12, "King":13}

    clsuitdict = {"Clubs":"c", "Diamonds":"d", "Hearts":"h", "Spades":"s"}

    # convert items in cardlist into a readable form for Card class (e.g. ['2', 'Spades'] to [2, 's'])  
    cardlist = [[clrankdict[i[0]],clsuitdict[i[1]]] for i in cardlist]
    
    # create list of card objects
    cardlist = [Card(i[0],i[1]) for i in cardlist]

    # get list of ranks and suits
    newlist = [[i.getRank(),i.getSuit()] for i in cardlist]

    # sort list by suit order
    sranklist = sorted(newlist)

    # convert ordered list of suits and ranks into card objects
    cardlist = [Card(i[0],i[1]) for i in sranklist]

    # convert list of card objects into list of strings
    strlist = [str(i) for i in cardlist]
    
    print(strlist)

    
    
main()
