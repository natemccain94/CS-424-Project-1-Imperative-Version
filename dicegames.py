# Nate McCain
# April 8, 2017
# CS 424 Section 01 (Tuesday/Thursday Section)
# This program allows two players to play either Fifty or Pig. It first asks for the players' names, and then
# which game they would like to play. After a game is won or lost, the players are asked if they would like
# to play either Fifty or Pig, or if they wish to end the program (This loop continues until a player decides
# to quit). Any time a player chooses to quit, the program ends (with a call "sys.exit()").
# Python 3.5.1
# Imperative Implementation

import random # Import the random.py library.
import sys # Import the sys.py library.

# This function prints the rules for playing Fifty.
# No parameters, no return values.
def print_instructions_for_fifty():
        print("Here are the instructions for Fifty.")
        print("Goal:")
        print("The goal of Fifty is to be the first player to reach 50 points. You get points by rolling doubles.")
        print("Play:")
        print("A turn consists of a player rolling a pair of dice (with the goal of rolling doubles), and scoring")
        print("the roll as described below. Play continues with each player taking one roll per turn. The first")
        print("player to score 50 or more points is declared the winner.")
        print("Scoring:")
        print("All doubles except 3's and 6's score 5 points. Double 6's are worth 25 points. Double 3's wipe")
        print("out the player's entire score, and the player must start again at 0. Non-double rolls are 0 points. \n")
        return
# End of function that prints the rules for Fifty.

# This function prints the rules for playing Pig.
# No parameters, no return values.
def print_instructions_for_pig():
        print("Here are the instructions for Pig.")
        print("Goal:")
        print("The goal of Pig is to be the first player to reach 100 points. You get points by rolling a single die")
        print("multiple times and adding the value on each roll of the die to your current score.")
        print("Play:")
        print("The first player rolls the die as many times as they want. The value of each throw is added onto")
        print("the score until the player decides to end his/her turn and passes the die to the next player. Play")
        print("continues until one player reaches 100.")
        print("Scoring:")
        print("The value of each throw is added to the current player's score. If the player rolls a 1, the player's")
        print("score goes back to 0, and their turn ends.")
        print("At one extreme, any player who gets a 1 on the first roll is immediately out. At the other extreme,")
        print("the first player could theoretically reach the winning score on the first turn, as long as they don't")
        print("roll a 1. If the player succeeds, the game ends there. \n")
        return
# End of function that prints the rules for Pig.

# This function indicates which player quit during a game. It is used by both games.
# It takes in the quitting player's name, and it makes a sys.exit() call (so no return values).
def playerQuitsDuringGame(playerName):
        print("Player " + playerName + " is a disgraceful quitter.")
        sys.exit()
# End of function that indicates the disgraceful quitter.

# This function is called when the players wish to end the program after playing one of the games.
# No parameters, and it makes a sys.exit() call (so no return values).
def playerQuitsAfterGame():
        print("Thank you for playing!")
        sys.exit()
# End of function that performs a graceful exit.

# This function is called when the players quit the program before any games have been played.
# No parameters, and it makes a sys.exit() call (so no return values).
def playerQuitsBeforeGameEvenStarts():
        print("You are really missing out by quitting before playing anything.")
        sys.exit()
# End of function that lets a player quit before having picked a game to play.

# Function that prints out the introductory message, and asks the players which game they want to play, or if they wish to
# end the program before any games are played.
# No parameters, and it returns a string containing the name of the game the players pick. 
def introductory_message():
        decision = False
        print_instructions_for_fifty()
        print_instructions_for_pig()
        while (decision == False):
                print("Please enter 'f' if you wish to play Fifty, or 'p' if you wish to play Pig.")
                print("If you wish to be a disgraceful quitter, please enter 'q'.\n")
                userInput = input()
                # If the players want to play Fifty
                if (userInput == 'f'):
                        return str("Fifty")
                # If the players want to play Pig
                elif (userInput == 'p'):
                        return str("Pig")
                # If the players want to end the program
                elif (userInput == 'q'):
                        playerQuitsBeforeGameEvenStarts()
                # Incorrect input
                else:
                        print("Incorrect input. Please follow the instructions.")
# End of introductory message function.

# Function that asks a player if they would like to play Fifty or Pig, only when at least one game has been played.
# It also asks if they would like to end the program.
# No parameters, returns the string containing the name of the game the players pick.
def playAgain():
        print("Would you like to continue playing games?")
        decision = False
        while (decision == False):
                print("Enter 'f' if you wish to play Fifty, or 'p' if you wish to play Pig.")
                print("Enter 'q' if you wish to quit the program.")
                userInput = input()
                # If the players want to play Fifty
                if (userInput == 'f'):
                        return str("Fifty")
                # If the players want to play Pig
                elif (userInput == 'p'):
                        return str("Pig")
                # If the players want to end the program
                elif (userInput == 'q'):
                        playerQuitsAfterGame()
                # Incorrect input
                else:
                        print("Incorrect input. Please follow the instructions.\n")
# End of function that asks if a player would like to keep playing the program

# This function indicates which player won the game.
# Parameters are the winning player's name and score. There are no return values.
def playerWins(playerName, playerScore):
        print("Player " + playerName + " wins with a score of ", playerScore, " points.\n")
        return
# End of function that indicates the winner.

# This function indicates which player lost by rolling a 1 with a score of 0. It is only used by Pig.
# Parameters are the losing player's name and the winning player's name. No return values.
def playerLoses(losingPlayer, winningPlayer):
        print("Player " + losingPlayer + " lost the game by rolling a 1 while their score was 0.")
        print(winningPlayer + " is the winner. \n")
        return
# End of function that indicates the loser.

# This function rolls a die. It's used by both games.
# No parameters, returns the result of the roll.
def rollDie():
        return random.randint(1,6) # Returns a random integer between 1 and 6.
# End of die rolling function.

# This function rolls the dice and changes the score accordingly when playing Fifty.
# It takes in the score from whichever player currently has their turn, and returns the player's updated score.
def executeRoll_fifty(playerScore):
        dieOne = int(rollDie())
        dieTwo = int(rollDie())
        print("You rolled a ", int(dieOne), " and a ", int(dieTwo), ".\n")
        # If doubles were rolled
        if (dieOne == dieTwo):
                # Double 3's
                if (dieOne == 3):
                        print("You rolled two 3's. You lose all of your points. \n")
                        playerScore = 0
                        return int(playerScore)
                # Double 6's
                elif (dieOne == 6):
                        print("You rolled two 6's. You get 25 points.\n")
                        playerScore += 25
                        return int(playerScore)
                # Other doubles rolled
                else:
                        print("You rolled two ", dieOne, "'s. You get 5 points. \n")
                        playerScore += 5
                        return int(playerScore)
        # Doubles were not rolled.
        else:
                print("You get zero points. \n")
                return int(playerScore)
# End of rolling the dice rolling function for the game fifty.

# This function rolls the die and changes the current player's score accordingly when playing Pig.
# It takes in the the name and score of whichever player currently has a turn, and returns their updated score.
def executeRoll_pig(playerName, playerScore):
        dieResult = int(rollDie())
        print("\n" + playerName + ", you rolled a ", dieResult, ".\n")
        
        # If the player rolls a 1,
        if (dieResult == 1):
                
                # and their score is zero, set score to -1 to indicate this player lost.
                if (int(playerScore) == 0):
                        playerScore = -1
                        return int(playerScore)
                
                # Else, set their score to zero.
                else:
                        playerScore = 0
                        return int(playerScore)
        
        # Otherwise, adjust their score accordingly.
        else:
                playerScore += dieResult
                return int(playerScore)
# End of function that executes a roll and changes a player's score when playing pig.

# This function gets the choice of what a player wants to do in a turn of Fifty.
# It takes in the player's name, and has no return values (it only returns to the calling function
# if the player chooses to roll, otherwise it makes a call to end the program).
def playerChoice_fifty(playerName):
        print("Player " + playerName + ", it is your turn. \n")
        
        decision = False
        while (decision == False):
                print("Enter 'r' to roll or 'q' to quit. \n")
                choice = input()
                # If the player wishes to roll the dice
                if (choice == 'r'):
                        print("Player " + playerName + " chooses to roll. \n")
                        decision = True
                # If the player wishes to end the program
                elif (choice == 'q'):
                        playerQuitsDuringGame(playerName)
                # Incorrect input
                else:
                        print("Player " + playerName + " does not know how to follow instructions. \n")
                        decision = False
        # End of while loop.
        
        return # Return to the calling function.
# End of function to get a player's choice for the game of fifty.

# This function asks a player what they want to do in a turn of Pig. They can choose to roll, end the turn (if not the start of a turn),
# or quit the program (makes a call to one of the exiting functions).
# Takes in the player's name and score, and a boolean indicating if it is the first roll of a player's turn.
# Returns True when a player chooses to roll, or False if they choose to end their turn (only after the first roll).
def get_player_choice_pig(playerName, playerScore, startOfTurn):
        decision = False
        # For the start of a player's turn
        while (startOfTurn == True):
                print(playerName + ", it is your turn.\n")
                print("You have ", playerScore, " points.\n")
                print("Enter 'r' to roll or 'q' to quit.\n")
                userInput = input()
                # Player wishes to roll the die
                if (userInput == 'r'):
                        return True
                # Player wishes to end the program
                elif (userInput == 'q'):
                        playerQuitsDuringGame(playerName)
                # Incorrect input
                else:
                        print("Please follow the instructions.\n")
        # End of while loop for the start of a player's turn.

        # When a player has already rolled once in the current turn
        while (startOfTurn == False):
                print(playerName + ", it is still your turn.\n")
                print("You have ", playerScore, " points.\n")
                print("Enter 'r' to roll, 'e' to end your turn, or 'q' to quit.\n")
                userInput = input()
                # Player wishes to roll the die
                if (userInput == 'r'):
                        return True
                # Player wishes to end their turn
                elif (userInput == 'e'):
                        return False
                # Player wishes to end the program
                elif (userInput == 'q'):
                        playerQuitsDuringGame(playerName)
                # Incorrect input
                else:
                        print("Please follow the instructions.\n")
        # End of while loop for after the first roll of a player's turn.
# End of function that gets a player's choice for what to do in a turn of pig.

# This function acts as a player's turn in Fifty.
# It takes in the player's name and score, and returns the player's updated score.
def playerTurn_fifty(playerName, playerScore):
        playerChoice_fifty(playerName)
        playerScore = int(executeRoll_fifty(playerScore))
        return int(playerScore)
# End of function that acts as a player's turn in fifty.

# This function acts as the control for a player's turn in Pig.
# It takes in the player's name and score, and the score needed to win Pig, and returns the player's updated score.
def playerTurn_pig(playerName, playerScore, winningScore):
        keepPlaying = bool(get_player_choice_pig(playerName, playerScore, True)) # Ask the player what to do at the beginning of their turn.
        playerScore = int(executeRoll_pig(playerName, playerScore)) # Get the updated player score
        keepPlaying = bool((playerScore != -1) and (playerScore < winningScore)) # True as long as the player has not lost or won.
        
        # What to do after the player's first roll, as long as the game is not over.
        while (keepPlaying == True):
                keepPlaying = bool(get_player_choice_pig(playerName, playerScore, False)) # Ask the player what they wish to do (not beginning of turn).
                # If the player wishes to keep rolling
                if (keepPlaying == True):
                        playerScore = int(executeRoll_pig(playerName, playerScore)) # Execute a roll and update their score.
                        keepPlaying = bool((playerScore != 0) and (playerScore < winningScore)) # Is the game over?
        # End of while loop.
        
        return int(playerScore) # Return the player's updated score.
# End of function that operates a player's turn in pig.

# This function runs the entire game of Fifty.
# It takes in the two players' names, and has no return values.
def playFifty(pOneName, pTwoName):
        print("Please allow me to remind you of the rules.\n")
        print_instructions_for_fifty()
        
        winningScore = 50 # This is the score needed to win the game.
        # Set both players' scores to 0.
        pOneScore = int(0)
        pTwoScore = int(0)
        gameOver = False
        
        # While the game has not ended
        while (gameOver == False):
                # Player one's turn.
                pOneScore = int(playerTurn_fifty(pOneName, int(pOneScore)))
                # If player one has won the game
                if (int(pOneScore) >= int(winningScore)):
                        print(pOneName + " has ", int(pOneScore), " and has won the game.\n")
                        gameOver = True
                        break
                # If player one has not won the game
                else:
                        print(pOneName + " has ", int(pOneScore), " points.\n")
                        gameOver = False
                        
                # Player two's turn.
                pTwoScore = int(playerTurn_fifty(pTwoName, int(pTwoScore)))
                # If player two has won the game
                if (int(pTwoScore) >= int(winningScore)):
                        print(pTwoName + " has ", int(pTwoScore), " and has won the game.\n")
                        gameOver = True
                        break
                # If player two has not won the game
                else:
                        print(pTwoName + " has ", int(pTwoScore), " points.\n")
                        gameOver = False
                        
        # end of while loop
        
        return # Return to the calling function.
# End of the function that runs the game fifty.

# This function runs the entire game of Pig.
# It takes in the two player's names, and has no return values.
def playPig(pOneName, pTwoName):
        print("Please allow me to remind you of the rules. \n")
        print_instructions_for_pig()
        
        winningScore = 100 # This is the score needed to win the game.
        # Set both players' scores to 0.
        pOneScore = int(0)
        pTwoScore = int(0)
        gameOver = False

        # While the game has not ended
        while (gameOver == False):
                # Player one's turn.
                pOneScore = int(playerTurn_pig(pOneName, pOneScore, winningScore))
                # If player one wins.
                if (pOneScore >= winningScore):
                        gameOver = True
                        playerWins(pOneName, pOneScore)
                        break
                # If player one loses.
                elif (pOneScore == -1):
                        gameOver = True
                        playerLoses(pOneName, pTwoName)
                        break

                # Player two's turn.
                pTwoScore = int(playerTurn_pig(pTwoName, pTwoScore, winningScore))
                # If player two wins.
                if (pTwoScore >= winningScore):
                        gameOver = True
                        playerWins(pTwoName, pTwoScore)
                        break
                # If player two loses.
                elif (pTwoScore == -1):
                        gameOver = True
                        playerLoses(pTwoName, pOneName)
                        break
        
            # End of while loop.
            
        return # Return to the calling function.
# End of function that runs the game pig.


# Function that is used to get a player's name.
# Takes in a string (it's either "Player One" or "Player Two"), and returns the string containing the player's name.
def getPlayerName(whichPlayer):
    print(whichPlayer + ", please type your name and press enter.")
    playerName = input()
    return playerName
# End of function used to get a player's name.

# This function is the project's driver. This acts as the controller for the entire project.
# It has no parameters, and no return values.
def main():
        print("Welcome to the boardgame collection! This program allows users to play either Fifty or Pig!\n")
        print("If at any point a player chooses to quit, the program will end. \n") # This is the warning about what quitting does.

        # Get the players' names
        playerOneName = str(getPlayerName("Player One"))
        playerTwoName = str(getPlayerName("Player Two"))
        
        infiniteLoopToKeepRunning = True
        gameToPlay = str(introductory_message()) # This asks for what game to play (when no games have yet been played).

        # While loop keeps the program going until somebody says they wish to quit.
        while (infiniteLoopToKeepRunning == True):
                # They want to play Fifty
                if (gameToPlay == "Fifty"):
                        print("You have chosen to play Fifty.\n")
                        playFifty(playerOneName, playerTwoName)
                # They want to play Pig
                else:
                        print("You have chosen to play Pig.\n")
                        playPig(playerOneName, playerTwoName)
                        
                gameToPlay = str(playAgain()) # Get what game they want to play (after at least one game has been played).
        # End of infinite while loop.
        
        return # This is just a formality, because this is meant to be an infinitely running loop.
# End of the function that holds my project together.

main() # Tells IDLE to call the driver function.
