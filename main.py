from game import *
from participants import Player

p = Player('Dor', 100)
p2 = Player('Shaked', 100)
p3 = Player('Inbar', 1000)
g = Game([p,p3])

while len(g.players) > 0:
    g.initialize_game()
    g.show_table()
    g.blackjack_logic()
    g.end_of_round()

