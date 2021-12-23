class Card:
    def __init__(self, cardNumber, color, sign):
        self.special = {1: 'A',
                        11: 'J',
                        12: 'Q',
                        13: 'K'}

        if cardNumber == 1:
            self.cardNumber = self.special[cardNumber]
            self.value = 11  # TODO: logic of Ace
        elif cardNumber in (11, 12, 13):
            self.cardNumber = self.special[cardNumber]
            self.value = 10
        else:
            self.cardNumber = cardNumber
            self.value = cardNumber

        self.color = color
        self.sign = sign

    def __str__(self):
        return '{} {} {}'.format(self.cardNumber, self.color, self.sign)

    def __eq__(self, other):
        return self.cardNumber == other.cardNumber and self.sign == other.sign
