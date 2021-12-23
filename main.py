from game import *
from participants import Player

p = Player('Dor', 100)
p2 = Player('Hadar', 100)
p3 = Player('Shlomi', 125)
g = Game([p, p2])

while len(g.players) > 0:
    g.initializeGame()
    g.showTable()
    g.blackjackLogic()
    g.endOfRound()

