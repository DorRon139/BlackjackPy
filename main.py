from game import *
from participants import Player

p = Player('Dor', 100)
p2 = Player('Shaked', 100)

g = Game([p])

while len(g.players) > 0:
    g.initialize_game()
    g.show_table()
    g.blackjack_logic()
    g.end_of_round()

