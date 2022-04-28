from card import Card
import random

class Deck:
    def __init__(self):
        self.deck = []
        for i in range(13):
            self.deck.append(Card(i+2, "Heart"))
            self.deck.append(Card(i+2, "Diamond"))
            self.deck.append(Card(i+2, "Club"))
            self.deck.append(Card(i+2, "Spade"))
    def shuffle(self):
        random.shuffle(self.deck)
    def drawCard(self):
        card = self.deck[0]
        self.deck.remove(card)
        return card

# deck = Deck()
# deck.shuffle()
# for i in range(52):
#     print(deck.deck[i])
# print("*****************************************")
# deck = Deck()
# for i in range(52):
#     print(deck.deck[i])