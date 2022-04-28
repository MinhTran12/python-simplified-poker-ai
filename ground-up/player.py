from card import Card
from handPotEval import HandPotEval
import utilities

class Player():
    def __init__(self, name, startChips):
        self.name = name
        self.chips = startChips
        self.card1 = None
        self.card2 = None
        self.handEval = HandPotEval()

    def GetChips(self):
        return self.chips
    
    def AddChips(self, chips):
        self.chips += chips
        return True
    
    def SubChips(self, chips):
        self.chips -= chips
        return True

    def GetCard1(self):
        return self.card1
    
    def GetCard2(self):
        return self.card2
    
    def GetRankOfHand(self, i_eval):
        if i_eval.type == 10:
            return "Royal Flush"
        elif i_eval.type == 9:
            return "Straight Flush"
        elif i_eval.type == 8:
            return "Four of a kind"
        elif i_eval.type == 7:
            return "Full House"
        elif i_eval.type == 6:
            return "Flush"
        elif i_eval.type == 5:
            return "A Straight"
        elif i_eval.type == 4:
            return "Three of a kind"
        elif i_eval.type == 3:
            return "Two pairs"
        elif i_eval.type == 2:
            return "One pair"
        else:
            return "Nothing"

    def EvaluateHand(self, cards):
        cardList = utilities.SortCards(cards)
        handCards = []
        handCards.append(self.card1)
        handCards.append(self.card2)
        handCards = utilities.SortCards(handCards)
        while True:
            if utilities.IsRoyalFlush(cardList):
                typeValue = 10
                break
            elif utilities.IsStraightFlush(cardList):
                typeValue = 9
                # highCard = cardList[4]
                break
            elif utilities.IsQuad(cardList):
                typeValue = 8
                # if cardList[3] == cardList[4]:
                #     highCard = cardList[4]
                # else:
                #     highCard = cardList[0]
                break
            elif utilities.IsFullHouse(cardList):
                typeValue = 7
                break
            elif utilities.IsFlush(cardList):
                typeValue = 6
                break
            elif utilities.IsStraight(cardList):
                typeValue = 5
                break
            elif utilities.IsTriple(cardList):
                typeValue = 4
                break
            elif utilities.IsTwoPairs(cardList):
                typeValue = 3
                break
            elif utilities.IsOnePair(cardList):
                typeValue = 2
                break
            else:
                typeValue = 1
                break

        # check for better hand
        if typeValue > self.handEval.type:
            self.handEval.type = typeValue