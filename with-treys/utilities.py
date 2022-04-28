from card import Card
from deck import Deck
from player import Player
from evaluator import Evaluator
import itertools

def OddCalculator(hand, board, deck):
    evaluator = Evaluator()
    wins = 0
    losses = 0
    draws = 0
    handStrength = evaluator.evaluate(hand, board)
    
    # create a list of possible opponent's hold cards from remaining cards in the deck
    possibleHoleCards = itertools.combinations(deck.cards, 2)
    
    for holeCards in possibleHoleCards:
        temp = [holeCards[0], holeCards[1]]                     # convert tuple to list
        possibleOpponentHS = evaluator.evaluate(temp, board)

        if handStrength < possibleOpponentHS:
            wins +=1
        elif handStrength > possibleOpponentHS:
            losses +=1
        else:
            draws +=1

    # calculate the win percentage out of all possible scenarios
    sumSimulation = wins + losses + draws
    winChance = float(wins/sumSimulation)

    return winChance

def CompareHands(player1, player2, board):
    evaluator = Evaluator()
    player1_HS = evaluator.evaluate(player1.hand, board)
    player2_HS = evaluator.evaluate(player2.hand, board)

    player1_HandType = evaluator.class_to_string(evaluator.get_rank_class(player1_HS))
    player2_HandType = evaluator.class_to_string(evaluator.get_rank_class(player2_HS))

    if player1_HS < player2_HS:
        print(player1.name + " wins!")
        player1.record[0] +=1
        player2.record[1] +=1
    elif player2_HS < player1_HS:
        print(player2.name + " wins!")
        player2.record[0] +=1
        player1.record[1] +=1
    else:
        print("It's a draw")
        player1.record[2] +=1
        player2.record[2] +=1
    
    return

def GetStats(player, computer, board):
    print("Board: " + Card.print_pretty_cards(board))
    print("Player's hand: "+ player.GetHand())
    print("Player's chips: " + str(player.chips))
    print("AI's chips: " + str(computer.chips))
    print("Player's current bet: " + str(player.currentBet))
    print("Pot size:" + str(player.currentBet + computer.currentBet))
    return

def PrintRecord(player1, player2):
    print(player1.name + "'s record W/L/D: " + str(player1.record[0]) + "/" + str(player1.record[1]) + "/"+ str(player1.record[2]))
    print(player2.name + "'s record W/L/D: " + str(player2.record[0]) + "/" + str(player2.record[1]) + "/"+ str(player2.record[2]))
    print("\n")
    return