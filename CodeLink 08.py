# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 8
# Connect Four Challenge
# last revised 12/25/24
#
# Using what we know about TicTacToe, can you finish writing the
# code to play Connect Four? You will want to replace my playRandomly()
# function with new versions of whatHappens() and findBestMove().
#
# Note that this version of the program joins a game that is almost
# finished.  Once your code works, remove a few checkers from that
# starting board and see what happens. How much slower is the code
# when the number of choices increases? Be careful; your computer might
# crash if you give it a fully blank board.

# import
import random

# constants
COMPUTERWINS = 1
PLAYERWINS = -1
TIE = 0
CONTINUE = 9999

# print the board nicely
def printBoard(board):

  print()
  print(" 1 2 3 4 5 6 7")

  for row in range(6):
    print (" ", end="")
    for col in range(1,8):
      print(board[row][col],end=" ")
    print()
  print()


# check for a completely filled board
def isFilled(board):

  emptySpaces = 42
  for col in range(1,8):
    emptySpaces -= board[6][col]
  if emptySpaces == 0:
    return True
  else:
    return False


# score the board
def scoreBoard(board):
  
  # return COMPUTERWINS if the computer won
  # return PLAYERWINS if the human won
  # return FILLED if there are no spaces left
  # otherwise CONTINUE the recursion

  # check for horizontal four-checker sequences
  for row in range(6):
    for col in range(1,5):
      if board[row][col] == board[row][col + 1] and board[row][col] == board[row][col + 2] and \
         board[row][col] == board[row][col + 3] and board[row][col] != "-":
        if board[row][col] == "C":
          return COMPUTERWINS
        else:
          return PLAYERWINS

  # check for vertical four-checker sequences
  for row in range(3):
    for col in range(1,8):
      if board[row][col] == board[row + 1][col] and board[row][col] == board[row + 2][col] and \
         board[row][col] == board[row + 3][col] and board[row][col] != "-":
        if board[row][col] == "C":
          return COMPUTERWINS
        else:
          return PLAYERWINS
      
  # check for diagonal four-checker sequences that run top-left to bottom-right
  for row in range(3):
    for col in range(1,5):
      if board[row][col] == board[row + 1][col + 1] and board[row][col] == board[row + 2][col + 2] and \
         board[row][col] == board[row + 3][col + 3] and board[row][col] != "-":
        if board[row][col] == "C":
          return COMPUTERWINS
        else:
          return PLAYERWINS

  # check for diagonal four-checker sequences that run top-right to bottom-left
  for row in range(3):
    for col in range(4, 8):
      if board[row][col] == board[row + 1][col - 1] and board[row][col] == board[row + 2][col - 2] and \
         board[row][col] == board[row + 3][col - 3] and board[row][col] != "-":
        if board[row][col] == "C":
          return COMPUTERWINS
        else:
          return PLAYERWINS
    
  # now check for a tie
  if isFilled(board):
    return TIE
  
  # if not, the board is still in play
  return CONTINUE


# generate a test board where we can test a proposed move
def generateTestBoard(board, col, player):

  # copy the board
  newBoard = []
  for oldRow in board:
    copiedRow = []
    for entry in oldRow:
      copiedRow.append(entry)
    newBoard.append(copiedRow)
    
  # put the correct mark at the proposed position
  newBoard = dropChecker(newBoard, player, col)
  
  return newBoard


# drop a checker onto the board
def dropChecker(board, symbol, col):

  firstEmptyRow = 5 - board[6][col]

  if firstEmptyRow != -1:
    board[firstEmptyRow][col] = symbol
    board[6][col] += 1

  else:
    print ("ERROR. Cannot drop checker in filled column.")

  return board


# accept only valid responses from the human player
def getPlayerMove(board):

  validChoice = False
  while not validChoice:
    
    response = input("Which column would you like? ")

    validChoice = True

    if response == "":
      validChoice = False
      print ("Please enter a column number.")
      
    else:

      chosenColumn = int(response)

      if chosenColumn not in [1, 2, 3, 4, 5, 6, 7]:
        validChoice = False
        print("That's not one of the options. Choose a number 1-7 please. ")

      elif board[6][chosenColumn] == 6:
        validChoice = False
        print("That column is already full. Please choose another one.")

  return chosenColumn


# decide what happens if this player makes this move
def whatHappens(board, column, player):

    # WRITE YOUR CODE HERE
    # ####################
    
    return    
  
# find the best move for this player
def findBestMove(board, player):

    # WRITE YOUR CODE HERE
    # ####################
    
    return

# for now, the computer moves randomly
def playRandomly(board):

  foundEmpty = False
  
  while not foundEmpty:
      possibleCol = random.randint(1,7)
      if board[6][possibleCol] < 6:
        foundEmpty = True

  return possibleCol

    
# ############
# main program

# notes:
# this is a partially filled board; we are joining the game in progress
# the bottom row is used to count the number of checkers in the above column
# players use columns 1-7; column 0 is not used

board = [
  [" ", "C", "C", "-", "-", "P", "P", "C"],
  [" ", "P", "P", "-", "-", "C", "C", "C"],
  [" ", "C", "C", "-", "-", "P", "P", "C"],
  [" ", "C", "P", "-", "-", "C", "C", "P"],
  [" ", "P", "P", "-", "-", "P", "P", "C"],
  [" ", "P", "C", "-", "-", "P", "P", "C"],
  [0,    6,   6,   0,   0,   6,   6,   6 ]
]

gameOver = False
humanTurn = True

print()
print("Let's play Connect Four.")
print()

while gameOver == False:

    printBoard(board)

    if humanTurn:
      humanColumn = getPlayerMove(board)     
      board = dropChecker(board, "P", humanColumn)
      if scoreBoard(board) == PLAYERWINS:
          printBoard(board)
          print("You win, human!")
          gameOver = True
      humanTurn = False

    else:
      print("The computer is moving randomly.")
      computerColumn = playRandomly(board)
      print ("Computer chooses column %d." % (computerColumn))
      board = dropChecker(board, "C", computerColumn)
      if scoreBoard(board) == COMPUTERWINS:
          printBoard(board)
          print("The computer wins!")
          gameOver = True
      humanTurn = True

    # check for a tie
    if isFilled(board):
      printBoard(board)
      print("Tie game.")
      gameOver = True

