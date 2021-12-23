from card import Card
from deck import Deck
import random

class Player:
    def __init__(self, name='user', coins=100):
        self.name = name
        self.coins = coins
        self.cards = []
        self.sum = self.getSum()
        self.inGame = True
        self.bet = 0

    def setCard(self, card):
        if isinstance(card, Card):
            self.cards.append(card)

    def getSum(self):
        for card in self.cards:
            self.sum += card.value
        return self.sum

    def __str__(self):
        back = "Player name: {}\nCoins: {}\nBet: {}\nCards:\n".format(self.name,self.coins,self.bet)
        for card in self.cards:
            back = back + '\t' + str(card) + '\n'
        back += "Value: {}\n".format(self.sum)
        return back


class Dealer:
    def __init__(self):
        self.dealerDeck = Deck().cardsToPlay
        self.cards = []
        self.sum = self.getSum()

    def handCard(self, target):
        cardToHand = random.choice(self.dealerDeck)
        self.dealerDeck.remove(cardToHand)
        target.setCard(cardToHand)
        return cardToHand

    def setCard(self, card):
        if isinstance(card, Card):
            self.cards.append(card)

    def getSum(self):
        for card in self.cards:
            self.sum += card.value
        return self.sum

    def __str__(self):
        back = "The Dealer's Cards:\n"
        for card in self.cards:
            back = back + str(card) + '\n'
        back += "The Dealer's Value: {}\n".format(self.sum)
        return back