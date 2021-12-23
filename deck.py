from card import *

class Deck():
    def __init__(self):
        self.types = ['Clubs','Spades','Diamonds','Hearts']
        self.colors = ['Red', "Black"]
        self.cardsToPlay = []
        for type in self.types:
            if(type == 'Diamonds' or type == 'Hearts' ):
                for i in range(1, 14):
                    self.cardsToPlay.append(Card(i, 'Red',type))
            if (type == 'Clubs' or type == 'Spades'):
                for i in range(1, 14):
                    self.cardsToPlay.append(Card(i, 'Black', type))
        for i in range(120):
            self.cardsToPlay.append(Card(1, 'Black', "type"))

    def removeCard(self, card):
        self.cardsToPlay.remove(card)

    def __str__(self):
        back = ''
        for card in self.cardsToPlay:
            back = back + str(card) + "\n"
        return back
