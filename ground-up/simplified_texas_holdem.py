from deck import Deck
from player import Player

class SimplifiedTexasHoldem():
    def __init__(self):
        self.players = []       # list of players
        self.deck = Deck()
        self.round = 0
        self.pot = 0
        self.nextTurn = 0       # decides which player goes next turn
                                # can only be either 0 or 1 for a 2-player game

        self.potCards = []      # list of pot cards

        self.end = False            # end of game
    
    def StartGame(self):
        self.players.append(Player("Player", 50))       # player 0 is the human player
        self.players.append(Player("AI", 50))           # player 1 is the AI

        self.deck.shuffle()
        for player in self.players:
            player.card1 = self.deck.drawCard()
            player.card1.onHand = True
            player.card2 = self.deck.drawCard()
            player.card2.onHand = True
        while len(self.potCards) < 5:
            self.potCards.append(self.deck.drawCard())
        
        return True
    
    def Raise(self, player, chips):
        if player.GetChips() < chips:
            return False
        else:
            player.SubChips(chips)
            self.pot += chips
        return True