class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        if self.rank < 11:
            self.rankName = str(self.rank)
        else:
            if self.rank == 11:
                self.rankName = "Jack"
            elif self.rank == 12:
                self.rankName = "Queen"
            elif self.rank == 13:
                self.rankName = "King"
            elif self.rank == 14:
                self.rankName = "Ace"
        self.suit = suit
    def __str__(self):
        return str(self.rankName) + " of " + str(self.suit)
    def __add__(self, other):
        return self.rank + other.rank