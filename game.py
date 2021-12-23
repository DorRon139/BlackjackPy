from deck import Deck
from participants import Player, Dealer
from card import Card


class Game:
    def __init__(self, playersList):
        self.dealer = Dealer()
        self.players = playersList

    def initialize_game(self):
        self.check_players()
        self.ask_for_bets()
        self.dealer.hand_card(self.dealer)
        for i in range(2):
            for player in self.players:
                self.dealer.hand_card(player)
        self.dealer.hand_card(self.dealer)
        for player in self.players:
            initialize_ace_logic(player)
        initialize_ace_logic(self.dealer)

    def check_players(self):
        for player in self.players:
            if player.coins == 0:
                print("{}, You can't play with no coins".format(player.name))
                self.players.remove(player)

    def ask_for_bets(self):
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

    def blackjack_logic(self):
        for player in self.players:
            self.player_turn(player)
        self.dealer_turn()
        for player in self.players:
            if self.check_winning(player):
                player.coins += 2 * player.bet

    def player_turn(self, player):
        options = {1: 'Stand', 2: 'Hit'}
        while player.sum < 21:
            print("{} Choose Your Move\n1.{} 2.{}".format(player.name, options[1], options[2]))
            decision = int(input())
            if decision == 1:
                break
            if decision == 2:
                card = self.dealer.hand_card(player)
                print(card)
                ace_logic_for_new_card(player)
                print("{}, Your Value is {}\n".format(player.name, player.sum))
                if player.sum > 21:
                    player.inGame = False
                    print("Burn")

    def dealer_turn(self):
        print("Dealer Turn: ")
        print("The Dealer Value is {}".format(self.dealer.sum))
        while self.dealer.sum <= 16:
            card = self.dealer.hand_card(self.dealer)
            print(card)
            ace_logic_for_new_card(self.dealer)
            print("The Dealer Value is {}".format(self.dealer.sum))

    def check_winning(self, player):
        if player.inGame:
            if self.dealer.sum < player.sum or self.dealer.sum > 21:
                print("{} Take Your Bet".format(player.name))
                return True
            print("You Lose, Thank you")
            return False

    def end_of_round(self):
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

    def show_table(self):
        print('\033[95m' + str(self.dealer))
        for player in self.players:
            print('\033[0m' + str(player))


def initialize_ace_logic(player):
    if player.cards[0].value == 11 and player.cards[1].value == 11:
        player.cards[0].value = 1
        player.sum -= 10


def ace_logic_for_new_card(player):
    i = 0
    while i < len(player.cards) and player.sum > 21:
        if player.cards[i].value == 11:
            player.cards[i].value = 1
            player.sum -= 10
            i += 1
        else:
            i += 1
