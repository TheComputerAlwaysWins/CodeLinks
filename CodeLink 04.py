# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 4
# Eight Queens
# last revised 5/6/26

# Using backtracking, can you find the 92 solutions to Eight Queens?
# You will need to write your own recursive function to replace the
# below playRandomly() function, but you might want to reuse my isLegal()
# to evaluate whether a specific placement is permissible.

import random

# FUNCTIONS

# print the board nicely
def printBoard(board):

    for row in range(0,8):
        for col in range(0,8):
            if board[row][col] == 0:
                print(" _ ", end="")
            if board[row][col] != 0:
                print(" %d " % board[row][col], end="")
        print("")
    print("")
    

# return True if this space is legal
def isLegal (board, possRow, possCol):

    # check this row
    for counter in range(0,8):
        if board[possRow][counter] >= 1:
            return False
                    
    # check this column
    for counter in range(0,8):
        if board[counter][possCol] >= 1:
            return False

    # check the diagonals from here, up left
    colCounter = possCol
    for rowCounter in range(possRow, 0, -1):
        if colCounter-1 >= 0:
            if board[rowCounter-1][colCounter-1] >= 1:
                return False
        colCounter = colCounter - 1
        
    # check the diagonal from here, up right
    colCounter = possCol
    for rowCounter in range(possRow, 0, -1):
        if colCounter+1 <= 7:
            if board[rowCounter-1][colCounter+1] >= 1:
                return False
        colCounter = colCounter + 1

    # check the diagonal from here, down left
    colCounter = possCol
    for rowCounter in range(possRow, 7):
        if colCounter-1 >= 0:
            if board[rowCounter+1][colCounter-1] >= 1:
                return False
        colCounter = colCounter-1
    
    # check the diagonal from here, down right
    colCounter = possCol
    for rowCounter in range(possRow, 7):
        if colCounter+1 <= 7:
            if board[rowCounter+1][colCounter+1] >= 1:
                return False
        colCounter = colCounter+1

    return True


def playRandomly (board):
# randomly place eight queens, and evaluate the board

    queensPlaced = 0
    success = True
    
    while queensPlaced < 8:

        randomCol = random.randint(0,7)
        randomRow = random.randint(0,7)

        if board[randomRow][randomCol] == 0:
            # found an empty space

            # test to see if placing a queen here causes a conflict
            if not isLegal(board, randomRow, randomCol):
                success = False

            # place the queen
            queensPlaced = queensPlaced + 1
            board[randomRow][randomCol] = queensPlaced
                
    printBoard(board)
    
    if success == True:
        print ("By sheer luck, I found a winning board!")
    else:
        print ("My random placement did not work out.")

    return


# main program
# ############

# Note that the board variable defined below has an extra row.
# I use positions board[0][0] through board[7][7],
# but I do not use board[8][0] through board [8][7].
# When you revise the code, feel free to use those extra spaces if you
# want to keep track of additional debug information about the game board.
# You also can just ignore them if you don't want to use them.

board[8].

board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]

print()
print("You will solve this problem using backtracking.")
print("Me? I am just trying random placements right now.")
print()

playRandomly(board)
print("")
    
