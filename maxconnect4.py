#Name : Jariwala Prayag
#UTA ID : 1001719373

#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

import sys
import time
from MaxConnect4Game import *

def oneMoveGame(currentGame, depth):
    start_time = time.time()
    if currentGame.pieceCount == 42:    # Is the board full already?
        print ('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)

    currentGame.aiPlay(depth) # Make a move (only random is implemented)

    print ('Game state after move:')
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()

    print("time taken by computer:" , time.time() - start_time)


def interactiveGame(currentGame, nextplayer, depth):
    # Fill me in
    #sys.exit('Interactive mode is currently not implemented')
    currentGame.printGameBoard()
    currentGame.countScore()
    print('Score:: Player-1 = %d, Player-2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
    if nextplayer == "human-next":
        while currentGame.getPieceCount() != 42:
            print("It is Human's turn.")
            humanmove = int(input("Enter Column number[1-7] to play: "))
            if not 0 < humanmove < 8:
                print("Column number must be between [1-7]")
                continue
            if not currentGame.playPiece(humanmove - 1):
                print("Column number: %d is full. Try another column." % humanmove)
                continue
            print("Your move is in column number:: " + str(humanmove))
            currentGame.printGameBoard()
            currentGame.gameFile = open("human.txt", 'w')
            currentGame.printGameBoardToFile()
            currentGame.gameFile.close()
            if currentGame.getPieceCount() == 42:
                print("BOARD FULL\n\nGame Over!\n")
                currentGame.countScore()
                print('Score:: Player-1 = %d, Player-2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
                break
            else:
                print("Computer is making a decision for next " + str(depth) + " steps...")
                if currentGame.currentTurn == 1:
                    currentGame.currentTurn = 2
                elif currentGame.currentTurn == 2:
                    currentGame.currentTurn = 1
                currentGame.aiPlay(depth)
                currentGame.printGameBoard()
                currentGame.gameFile = open('computer.txt', 'w')
                currentGame.printGameBoardToFile()
                currentGame.gameFile.close()
                currentGame.countScore()
                print('Score:: Player-1 = %d, Player-2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
    else:
        currentGame.aiPlay(depth)
        currentGame.gameFile = open('computer.txt', 'w')
        currentGame.printGameBoardToFile()
        currentGame.gameFile.close()
        currentGame.printGameBoard()
        currentGame.countScore()
        print('Score:: Player-1 = %d, Player-2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
        interactiveGame(currentGame, 'human-next', depth)

    if currentGame.getPieceCount() == 42:
        if currentGame.player1Score > currentGame.player2Score:
            print("Player 1 won the Game !")
        if currentGame.player1Score == currentGame.player2Score:
            print("The game is a Tie !")
        if currentGame.player1Score < currentGame.player2Score:
            print("Player 2 won the Game !")
        print("Game Over")


def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print ('Four command-line arguments are needed:')
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print ('\nMaxConnect-4 game\n')
    print ('Game state before move:')
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        interactiveGame(currentGame, argv[3], int(argv[4])) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame,int(argv[4])) # Be sure to pass any other arguments from the command line you might need.

main(sys.argv)

#References
#GeeksforGeeks
#Github
#AI-Stuart Russell and Peter Norvig 3rd Edition