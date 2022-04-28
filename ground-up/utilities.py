from card import Card

def SortCards(cardList):
    newCardList = cardList
    for i in range(len(newCardList)-1):
        if newCardList[i].rank > newCardList[i+1].rank:
            temp = newCardList[i]
            newCardList[i] = newCardList[i+1]
            newCardList[i+1] = temp
    return newCardList

def IsOnePair(sortedCardList):
    if IsFullHouse(sortedCardList) or IsQuad(sortedCardList) or IsTriple(sortedCardList) or IsTwoPairs(sortedCardList):
        return False
    for i in range(len(sortedCardList)-1):
        if sortedCardList[i].rank == sortedCardList[i+1].rank:
            return True
    return False
    
def IsTwoPairs(sortedCardList):
    if IsFullHouse(sortedCardList) or IsQuad(sortedCardList) or IsTriple(sortedCardList):
        return False
    value1 = sortedCardList[0].rank == sortedCardList[1].rank and sortedCardList[3].rank == sortedCardList[4].rank
    value2 = sortedCardList[0].rank == sortedCardList[1].rank and sortedCardList[2].rank == sortedCardList[3].rank
    value3 = sortedCardList[1].rank == sortedCardList[2].rank and sortedCardList[3].rank == sortedCardList[4].rank
    return value1 or value2 or value3

def IsTriple(sortedCardList):
    value1 = sortedCardList[0].rank == sortedCardList[1].rank == sortedCardList[2].rank
    value2 = sortedCardList[1].rank == sortedCardList[2].rank == sortedCardList[3].rank
    value3 = sortedCardList[2].rank == sortedCardList[3].rank == sortedCardList[4].rank
    return value1 or value2 or value3

def IsStraight(sortedCardList):
    for i in range(len(sortedCardList)-1):
        if sortedCardList[i].rank + 1 == sortedCardList[i+1].rank:
            value = True
        else:
            value = False
    return value

def IsFlush(cardList):
    for i in range(len(cardList)-1):
        if cardList[i].suit == cardList[i+1].suit:
            value = True
        else:
            value = False
    return value

def IsFullHouse(sortedCardList):
    value1 = sortedCardList[0].rank == sortedCardList[1].rank == sortedCardList[2].rank and sortedCardList[3].rank == sortedCardList[4].rank
    value2 = sortedCardList[0].rank == sortedCardList[1].rank and sortedCardList[2].rank == sortedCardList[3].rank == sortedCardList[4].rank
    return value1 or value2

def IsQuad(sortedCardList):
    value1 = sortedCardList[0].rank == sortedCardList[1].rank == sortedCardList[2].rank == sortedCardList[3].rank
    value2 = sortedCardList[1].rank == sortedCardList[2].rank == sortedCardList[3].rank == sortedCardList[4].rank
    return value1 or value2

def IsStraightFlush(sortedCardList):
    return IsFlush(sortedCardList) and IsStraight(sortedCardList)

def IsRoyalFlush(sortedCardList):
    if IsStraightFlush(sortedCardList) and sortedCardList[4].rank == 14:
        return True
    return False