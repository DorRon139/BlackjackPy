from deck import Deck
from participants import Player,Dealer
from card import Card


class Game():
    def __init__(self, playersList):
        self.dealer = Dealer()
        self.players = playersList

    def initializeGame(self):
        self.checkPlayers()
        for player in self.players:
            print("{} Place Your Bet: ".format(player.name))
            player.bet = int(input())
            if player.bet == 0:
                print("See You Next Time {}".format(player.name))
            else:
                while player.bet < 0 or player.bet > player.coins:
                    if player.bet < 0:
                        print("Min Bet is 1$")
                    if player.bet > player.coins:
                        print("You D'ont Have {}$".format(player.bet))
                    player.bet = int(input())
            player.coins -= player.bet
        for player in self.players:
            if player.bet == 0:
                self.players.remove(player)

        self.dealer.handCard(self.dealer)
        for i in range(2):
            for player in self.players:
                self.dealer.handCard(player)
        self.dealer.handCard(self.dealer)

    def showTable(self):
        print('\033[95m' + str(self.dealer))
        for player in self.players:
            print('\033[0m' +str(player))

    def checkPlayers(self):
        for player in self.players:
            if player.coins == 0:
                print("{}, You can't play with no coins".format(player.name))
                self.players.remove(player)


    def blackjackLogic(self):
        for player in self.players:
            self.playerTurn(player)
        self.dealerTrun()
        for player in self.players:
            if(self.checkWinning(player)):
                player.coins += 2*player.bet

    def playerTurn(self,player):
        options = {1: 'Stand', 2: 'Hit'}
        decision = 2
        while decision == 2 and player.sum < 21:
            print("{} Choose You Move\n1.{} 2.{}".format(player.name, options[1], options[2]))
            decision = int(input())
            if decision == 2:
                card = self.dealer.handCard(player)
                print(card)
                print("{}, Your Value is {}\n".format(player.name, player.sum))
                if player.sum > 21:
                    player.inGame = False
                    print("Burn")



    def dealerTrun(self):
        print("Dealer Turn: ")
        print("The Dealer Value is {}".format(self.dealer.sum))
        while self.dealer.sum <= 16:
            card = self.dealer.handCard(self.dealer)
            print(card)
            print("The Dealer Value is {}".format(self.dealer.sum))

    def checkWinning(self, player):
        if player.inGame:
            if self.dealer.sum < player.sum or self.dealer.sum > 21:
                print("{} Take Your Bet".format(player.name))
                return True
            print("You Lose, Thank you")
            return False

    def endOfRound(self):
        for player in self.players:
            for card in player.cards:
                self.dealer.dealerDeck.append(card)
            player.cards.clear()
            player.sum = 0
            player.inGame = True
        for card in self.dealer.cards:
            self.dealer.dealerDeck.append(card)
            self.dealer.cards.clear()
            self.dealer.sum = 0
        print("**End Of Round**")