

class Card():
    def __init__(self, number, color, sign):
        self.value = int(number)
        self.spacials = { 1:'A',
                         11:'J',
                         12:'Q',
                         13:'K'}


        if number == 1:
            self.number = self.spacials[number]
            self.value = 11  #TODO: logic of Ace
        elif number in (11,12,13):
            self.number = self.spacials[number]
            self.value = 10
        else:
            self.number = number
        self.color = color
        self.sign = sign

    def isAce(self,player):
        if self.value == 1:
            if player.sum <= 10:
                self.value = 11

    def __str__(self):
        return '{} {} {}'.format(self.number, self.color, self.sign)

    def __eq__(self, other):
        return ((self.number == other.number) and (self.sign == other.sign))