from card import Card
from deck import Deck
import random


class Player:
    def __init__(self, name='user', coins=100):
        self.name = name
        self.coins = coins
        self.cards = []
        self.sum = 0
        self.inGame = True
        self.bet = 0

    def set_card(self, card):
        if isinstance(card, Card):
            self.cards.append(card)
            self.sum += card.value

    def count_sum(self):
        for card in self.cards:
            self.sum += card.value

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
        self.sum = 0

    def hand_card(self, target):
        cardToHand = random.choice(self.dealerDeck)
        self.dealerDeck.remove(cardToHand)
        target.set_card(cardToHand)
        return cardToHand

    def set_card(self, card):
        if isinstance(card, Card):
            self.cards.append(card)
            self.sum += card.value

    def __str__(self):
        back = "The Dealer's Cards:\n"
        for card in self.cards:
            back = back + str(card) + '\n'
        back += "The Dealer's Value: {}\n".format(self.sum)
        return back