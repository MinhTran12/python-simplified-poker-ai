from deck import Deck
from card import Card
from player import Player
import random
import utilities
from evaluator import Evaluator

handEvaluator = Evaluator()

class TexasHoldem():
    def __init__(self, cheat):
        self.players = []           # list of players
        self.deck = []              # empty deck
        self.twoAIs = False         # for AI vs AI
        self.printOddsAI = cheat    # prints AI's chance of winning    
        self.round = 0
        self.pot = 0
        self.turn = -1              # decides whose turn is it
        self.first = -1             # decides which player goes first in a round
        self.board = []             # list of cards on the board
    
    def StartGame(self):
        print("Welcome to Texas Holdem Poker!\n")
        command = input("Do you want the AI to play against itself? (y/n) ")
        if command == "y":
            print("AI vs Ai is now enabled.\n")
            self.twoAIs = True
        else:
            print("AI vs AI is not enabled.")
            print("Maximum bet size is 7 chips.\n")

        self.players.append(Player("Player", 10000))       # player 0 is the human player
        self.players.append(Player("AI", 10000))           # player 1 is the AI

        self.NewGame()

        return True
    
    def NewGame(self):
        self.deck = Deck()                      # is shuffled when initialized

        self.players[0].hand = self.deck.draw(2)
        self.players[1].hand = self.deck.draw(2)

        self.board = self.deck.draw(3)          # 3 cards at the beginning
        
        self.round = 1
        self.first = random.choice([0,1])       # random who goes first
        self.turn = self.first

        self.players[0].currentBet = 0               
        self.players[1].currentBet = 0

        self.Round()

        return True

    def Round(self):

        self.players[0].action = 0
        self.players[1].action = 0

        print("Round " + str(self.round) + "\n")
        if self.players[0] == self.players[self.first]:
            print("Player goes first")
        else:
            print("AI goes first")

        print("Board:" + Card.print_pretty_cards(self.board) + "\n")
        print("Player's hand: " + self.players[0].GetHand())

        while not((self.players[0].action == 2 and self.players[1].action == 2)
                    or self.players[0].action == 3
                    or self.players[1].action == 3
                    or self.players[0].action == 4
                    or self.players[1].action == 4):
            if self.turn == 0:
                if self.twoAIs == True:
                    self.ComputerAction(self.players[0], self.players[1])
                else:
                    self.PlayerAction(self.players[0], self.players[1])
                self.turn = 1
            else:
                self.ComputerAction(self.players[1], self.players[0])
                self.turn = 0
        print("****************************************")
        if self.players[0].action == 4 or self.players[1].action == 4:
            self.NewGame()
        else:
            self.round += 1
            self.NextRound()
        return True
    
    def NextRound(self):
        # showdown if round > 3
        if self.round == 4:
            print("Board:" + Card.print_pretty_cards(self.board) + "\n")
            print("Player's hand: " + self.players[0].GetHand())
            print("AI's hand: " + self.players[1].GetHand())

            utilities.CompareHands(self.players[0], self.players[1], self.board)
            utilities.PrintRecord(self.players[0], self.players[1])

            print("Do you wish to continue playing?")
            command = input("y/n (case sensitive): ")
            if command == "y":
                self.NewGame()
            else:
                print("Thank you for playing")
        else:
            self.board.append(self.deck.draw())
            self.turn = self.first
            self.Round()
        return

    def Raise(self, player, opponent, chips):
        # call then raise
        totalBet = chips + opponent.currentBet
        
        if chips > 7:
            print("Maximum bet size is 7 chips")
            return False
        elif chips <= 0:
            print("Chips raised cannot be equal to or less than 0")
            return False
        elif player.chips < totalBet:
            print(player.name + " doesn't have enough chips")
            return False
        else:
            print(player.name + " raises " + str(chips) + " chips.")
            player.SubChips(totalBet - player.currentBet)
            player.currentBet = totalBet
            self.pot += totalBet
            player.action = 1
        return True

    def Call(self, player, opponent):
        print(player.name + " calls.")
        chips = opponent.currentBet - player.currentBet
        player.SubChips(chips)
        player.currentBet += chips
        self.pot += chips
        player.action = 3
        return True

    def Check(self, player):
        print(player.name + " checks.")
        player.action = 2
        return True
    
    def Fold(self, player, opponent):
        print(player.name + " folds.")
        player.SubChips(player.currentBet)
        opponent.AddChips(self.pot)
        player.action = 4
        player.record[1] += 1
        opponent.record[0] += 1
        utilities.PrintRecord(player, opponent)
        return True
    
    def PlayerAction(self, player, opponent):
        print("Possible actions: raise, check, call, fold, getstat.")
        command = input("Enter input (case sensitive): ")
        if command == "raise":
            chips = int(input("How many chips? "))
            action = self.Raise(player, opponent, chips)
            if action == False:
                print("Amount of chips not valid.")
                return self.PlayerAction(player, opponent)
        elif command == "check":
            if opponent.action != 0 and opponent.action != 2:
                print("You can only check first turn or when your opponent just checked. \n")
                return self.PlayerAction(player, opponent)
            self.Check(player)
        elif command == "call":
            if opponent.action == 0 or opponent.action == 2:
                print("Can't call when going first or after an opponent's check.\n")
                return self.PlayerAction(player, opponent) 
            self.Call(player, opponent)
        elif command == "fold":
            self.Fold(player, opponent)
        elif command == "getstat":
            utilities.GetStats(player, opponent, self.board)
            return self.PlayerAction(player, opponent)
        else:
            print("Unrecognized command.")
            return self.PlayerAction(player, opponent)
        return True
    
    def ComputerAction(self, playerAI, opponent):
        winChance = utilities.OddCalculator(playerAI.hand, self.board, self.deck)
        x = random.random()

        # cheat enabled
        if self.printOddsAI == True:
            print(str(winChance))

        # possible actions: raise, call, fold
        if opponent.action == 1:
            if winChance >= 0.85:
                if x >= 0.6:
                    self.Raise(playerAI, opponent, random.randint(4, 7))
                elif x >= 0.3:
                    self.Raise(playerAI, opponent, random.randint(3, 6))
                else:
                    self.Call(playerAI, opponent)
            elif winChance >= 0.65:
                if x >= 0.65:
                    self.Raise(playerAI, opponent, random.randint(3, 5))
                elif x >= 0.35:
                    self.Raise(playerAI, opponent, random.randint(2, 4))
                else:
                    self.Call(playerAI, opponent) 
            elif winChance >= 0.45:
                if x >= 0.8:
                    self.Raise(playerAI, opponent, random.randint(2, 4))
                elif x >= 0.6:
                    self.Raise(playerAI, opponent, random.randint(1, 3))
                elif x >= 0.05:
                    self.Call(playerAI, opponent)
                else:
                    self.Fold(playerAI, opponent)
            elif winChance >= 0.30:
                if x >= 0.85:
                    self.Raise(playerAI, opponent, random.randint(1, 2))
                elif x >= 0.7:
                    self.Call(playerAI, opponent)
                else:
                    self.Fold(playerAI, opponent)
            else:
                if x >= 0.95:
                    self.Raise(playerAI, opponent, 1)
                elif x >= 0.85:
                    self.Call(playerAI, opponent)
                else:
                    self.Fold(playerAI, opponent)
        # possible actions: raise, check, fold
        elif opponent.action == 0 or opponent.action == 2:
            if winChance >= 0.85:
                if x >= 0.6:
                    self.Raise(playerAI, opponent, random.randint(4, 7))
                elif x >= 0.3:
                    self.Raise(playerAI, opponent, random.randint(3, 6))
                else:
                    self.Check(playerAI)
            elif winChance >= 0.65:
                if x >= 0.65:
                    self.Raise(playerAI, opponent, random.randint(3, 5))
                elif x >= 0.35:
                    self.Raise(playerAI, opponent, random.randint(2, 4))
                else:
                    self.Check(playerAI) 
            elif winChance >= 0.45:
                if x >= 0.8:
                    self.Raise(playerAI, opponent, random.randint(2, 4))
                elif x >= 0.6:
                    self.Raise(playerAI, opponent, random.randint(1, 3))
                elif x >= 0.03:
                    self.Check(playerAI)
                else:
                    self.Fold(playerAI, opponent)
            elif winChance >= 0.30:
                if x >= 0.85:
                    self.Raise(playerAI, opponent, random.randint(1, 2))
                elif x >= 0.7:
                    self.Check(playerAI)
                else:
                    self.Fold(playerAI, opponent)
            else:
                if x >= 0.95:
                    self.Raise(playerAI, opponent, 1)
                elif x >= 0.85:
                    self.Check(playerAI)
                else:
                    self.Fold(playerAI, opponent)
        return True
    