from card import Card

class Player():
    def __init__(self, name, startChips):
        self.name = name
        self.chips = startChips
        self.hand = []
        self.record = [0,0,0]
        self.currentBet = 0
        self.action = 0         # 1 raise
                                # 2 check
                                # 3 call
                                # 4 fold
                                # 0 no action
    
    def AddChips(self, chips):
        self.chips += chips
        return True
    
    def SubChips(self, chips):
        self.chips -= chips
        return True

    def GetHand(self):
        return Card.print_pretty_cards(self.hand)