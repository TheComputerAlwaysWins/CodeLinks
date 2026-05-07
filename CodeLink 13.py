# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 13
# Aim-the-Darts Blackjack
# last revised 5/6/26
#
# This code starts by playing just a few games, showing you the cards
# so that you can evaluate the computer's decisions.  After that, the
# code simulates 1000 games so that you can evalute the algorithm.
#
# Note that you can change the number of sample games, the number of
# simulations run, and so on.  Just adjust the correct variable in the
# block of definitions immediately below this note.

import random
# import math

# global definitions
hidden = True           # there is a hidden card on the table
final = True            # this is a final hand, not a hand in progress
simulationsMax = 1000   # how many simulations are allowed before the computer must move
gamesTotal = 1000       # how many rounds of BlackJack to play in the simulation
sampleGames = 5         # how many sample games to display on the screen
STAND = 0               # a constant
TAKE = 1                # a constant


      
# printing functions

def nicePrint (values):
    for item in values:
        print ("%6d " %item, end="")
    print ("")
    
def nicePrintCard (card):
    if card == 1:
        print("A ", end="")
    elif card == 11:
        print ("J ", end="")
    elif card == 12:
        print ("Q ", end="")
    elif card == 13:
        print ("K ", end="")
    else:
        print ("%d " %card, end="")

def nicePrintHand (hand):
    for card in hand:
        nicePrintCard(card)
    print ("")

    
# card handling functions
    
def newCard(deck):
    # receives deck of cards as an array, using positions 1 through 13, with possibly some removed
    # returns the array number of the card to offer (1=Ace, 11=Jack, 12=Queen, 13=King)

    # count how many cards are left in the deck

    cardsLeft = 0
    for counter in range(1,14):
        cardsLeft = cardsLeft + deck[counter]

    # choose one
    nextCard = random.randint(1,cardsLeft)

    # identify it; for example, if there are 4 aces then card 5 is a 2
    cardsSeen = 0
    position = 1
    while (cardsSeen + deck[position]) < nextCard:
        cardsSeen = cardsSeen + deck[position]
        position += 1

    # remove that card from the deck
    deck[position] = deck[position] - 1

    return position

            
def valueHand(hand):
    # score the hand
     
    value = 0
    hasAce = False

    for card in hand:
        if card == 1:
            hasAce = True           
        else:
            if card >= 10:
                value = value + 10
            else:
                value = value + card

    if hasAce == True:
        # treat an ace as 11, unless that causes a bust
        
        if (value + 11) > 21:
            value = value + 1
        else:
            value = value + 11

    return value


def makeHand(cards):
    # create a copy of the hand so that the code can experiment with it

    hand = []

    for counter in range(len(cards)):
        hand.append(cards[counter])

    return hand


def makeDeck(computerCards, dealerCards, isHidden):
    # create a copy of the deck so that the code can experiment with it
    # be sure to remove cards that are already known to be used
    # during simulations, the hidden card is not known and so not removed
    
    # create a new 52-card deck
    deck = []
    deck.append(0)                    # don't use the 0 location
    for counter in range(1,14):       # 1 = Ace, 2 = 2, 3 = 3, ... 11 = J, 12 = Q, 13 = K
        deck.append(4)

    for card in computerCards:
        deck[card] = deck[card]-1

    if isHidden:
        # remove only the revealed card from the deck
        revealedCard = dealerCards[0]
        deck[revealedCard] = deck[revealedCard] - 1
    else:
        # remove all used cards
        for card in dealerCards:
            deck[card] = deck[card]-1
 
    return deck



def scoreGame(computerHand, dealerHand):
    # return 1 if computer won
    # return 0 otherwise
    # doug change: -1 if loss, so similar to connect four code

    computerScore = valueHand(computerHand)
    dealerScore = valueHand(dealerHand)

    if computerScore > 21:
        return -1

    if dealerScore > 21:
        return 1

    if computerScore > dealerScore:
        return 1

    if computerScore < dealerScore:
        return -1

    else:
        if computerScore != dealerScore:
            print ("Error: ScoreGame expected a tie here.")
        return 0
    


def playRandomly (computerCards, dealerCards):

    # make local copy of hand to experiment with
    computerHand = makeHand(computerCards)
        
    # computer is done if reached 21, or busted
    if (valueHand(computerHand) > 20):
        finished = True
    else:
        finished = False

    while not finished:

        # make a deck to work with; note: the dealer has a hidden card
        deck = makeDeck(computerHand, dealerCards, hidden)
     
        # randomly choose to take(0) or stand(1)
        chosenMove = random.randint(0,1)

        if chosenMove == 0:
            # take
            drawnCard = newCard(deck)
            computerHand.append(drawnCard)

        else:
            # stand
            finished = True

        if valueHand(computerHand)>20:
            finished = True

    # create a  local version of the dealer's hand to experiment with
    dealerHand = makeHand(dealerCards)
    
    # the dealer plays until 17 in response
    dealerHand = playTo17(computerHand, dealerHand, hidden)

    return scoreGame(computerHand, dealerHand)


def playTo17(computerCards, dealerCards, isHidden):
    # computer plays until 17 or more

    # make local hand and deck to experiment with
    dealerHand = makeHand(dealerCards)
    
    if isHidden:
        # simulate as if the hidden card is not in the dealer's hand
        deck = makeDeck (computerCards, dealerHand, hidden)
        hiddenCard = dealerCards[1]
        dealerHand.remove(hiddenCard)
                
    else:
        # actually playing now, so hidden card is known
        deck = makeDeck(computerCards, dealerCards, not hidden)
        
    dealerScore = valueHand(dealerHand)

    while dealerScore < 17:
        drawnCard = newCard(deck)
        dealerHand.append(drawnCard)
        dealerScore = valueHand(dealerHand)
        deck[drawnCard]-= 1

    return dealerHand
    

def isStand (node):

    if node == 1:
        return False
    
    if node%2 == 0:
        return False

    else:
        return True

        
def chooseChild (nodeNum, takeWins, takeVisits, standWins, standVisits):

    # identify the take and stand children nodes
    if nodeNum != 1:
        nextTake = nodeNum + 2
        nextStand = nodeNum + 3
    else:
        nextTake = nodeNum + 1
        nextStand = nodeNum + 2

    # favor unvisited nodes
    if takeVisits == 0:
        return nextTake

    if standVisits == 0:
        return nextStand

    # if both visited, calculate win rates
    winRateTake = takeWins/takeVisits
    winRateStand = standWins/standVisits

    # score the nodes
    totalVisits = standVisits + takeVisits
    takeScore = 5 * winRateTake + (totalVisits/takeVisits)**.5
    standScore = 5 * winRateStand + (totalVisits/standVisits)**.5

    if takeScore > standScore:
        return nextTake
    else:
        return nextStand
         
                                                                                                                                                                                                
def findBestMove (computerCards, dealerCards):

    # create the deck of cards and simulation counter
    deck = makeDeck(computerCards, dealerCards, hidden)
    simulationsRun = 0

    # create two practice hands
    computerHand = makeHand(computerCards)
    dealerHand = makeHand(dealerCards)

    # initialize node variables for node 0 (ignore) and node 1 (root)
    visits = [0,0]
    wins = [0,0]
    
    # point to the root
    currentNode = 1
    
    while simulationsRun < simulationsMax:

        if isStand(currentNode):

            # draw enough cards to reach this node
            cardsTaken = int((currentNode-3)/2)
            for counter in range(cardsTaken):
                drawnCard = newCard(deck)
                computerHand.append(drawnCard)

            # randomly simulate the dealer's moves, and determine winner
            dealerHand = playTo17(computerHand, dealerHand, hidden)
            result = scoreGame(computerHand, dealerHand)
            simulationsRun += 1 

            # add visit and result to this node
            visits[currentNode] = visits[currentNode] + 1
            wins[currentNode] = wins[currentNode] + result

            # add visit and result to the nodes that led here
            if currentNode > 3:
                currentNode = currentNode - 3
                while currentNode>1:
                    visits[currentNode] = visits[currentNode] + 1
                    wins[currentNode] = wins[currentNode] + result
                    currentNode = currentNode - 2
            visits[1] = visits[1] + 1
            wins[1] = wins[1] + result
        
            # reset computer hand, dealer hand, and deck for future simulations
            computerHand = makeHand(computerCards)
            dealerHand = makeHand(dealerCards)
            deck = makeDeck(computerCards, dealerCards, hidden)
            
            # reset currentNode to the starting point
            currentNode = 1

        elif visits[currentNode] == 0:
            # this is a new "take" node

            # prepare for the next level of the tree
            visits.append(0)
            visits.append(0)
            wins.append(0)
            wins.append(0)
            
            # draw enough cards to reach this node
            cardsTaken = int(currentNode/2)
            for counter in range(cardsTaken):
                drawnCard = newCard(deck)
                computerHand.append(drawnCard)

            # randomly simluate a game
            result = playRandomly(computerHand, dealerHand)
            simulationsRun += 1 
         
            # add visit and result to this node
            visits[currentNode] = visits[currentNode] + 1
            wins[currentNode] = wins[currentNode] + result
            
            # add visit and result to the nodes that led here
            currentNode = currentNode - 2
            while currentNode > 1:
                visits[currentNode] = visits[currentNode] + 1
                wins[currentNode] = wins[currentNode] + result
                currentNode = currentNode - 2
            if currentNode == 0:
                visits[1] = visits[1] + 1
                wins[1] = wins[1] + result

            # again, reset the various variables
            computerHand = makeHand(computerCards)
            dealerHand = makeHand(dealerCards)
            deck = makeDeck(computerCards, dealerCards, hidden)
            currentNode = 1

        else:
            # gather data about the two child nodes
            if currentNode != 1:
                takeWins = wins[currentNode+2]
                takeVisits = visits[currentNode+2]
                standWins = wins[currentNode+3]
                standVisits = visits[currentNode+3]
            else:
                takeWins = wins[currentNode+1]
                takeVisits = visits[currentNode+1]
                standWins = wins[currentNode+2]
                standVisits = visits[currentNode+2]

            # pick one
            nextNode = chooseChild(currentNode, takeWins, takeVisits, standWins, standVisits)
            currentNode = nextNode
   
    # simulation is over
    # choose between node 2 and node 3
    winRateTake = wins[2]/visits[2]
    winRateStand = wins[3]/visits[3]

    # return our choice    
    if winRateTake > winRateStand:
        return TAKE
    else:
        return STAND
    

# ############
# main program
# ############

# first, play a few games on the screen

for samples in range(sampleGames):
   
    # no one has cards yet
    computerHand = []
    dealerHand = []
      
    # create a new 52-card deck
    deck = makeDeck(computerHand, dealerHand, not hidden)
    
    # give the computer one card
    takeCard = newCard(deck)
    computerHand.append(takeCard)
    deck[takeCard] -=1

    # give the dealer their revealed card
    takeCard = newCard(deck)
    dealerHand.append(takeCard)
    deck[takeCard] -=1

    # give the computer their second card
    takeCard = newCard(deck)
    computerHand.append(takeCard)
    deck[takeCard] -=1

    # give the dealer their secret card
    takeCard = newCard(deck)
    dealerHand.append(takeCard)
    deck[takeCard] -=1

    # let the computer play
    finished = False
    while not finished:
                
        if (findBestMove(computerHand, dealerHand) == TAKE):
            takeCard = newCard(deck)
            deck[takeCard] = deck[takeCard] - 1
            computerHand.append(takeCard)

        else:
            finished = True

        # check to see if we should stop
        if valueHand(computerHand) > 20:
            finished = True

    # dealer now can take more cards, up to 17        
    dealerHand = playTo17(computerHand, dealerHand, not hidden)

    # show the game on the screen
    print("")
    print("SAMPLE GAME %d" % (samples+1))
    print ("  Computer: ", end="")
    nicePrintHand(computerHand)
    print ("  Dealer:   ", end="")
    nicePrintHand(dealerHand)
    
    # see who won
    result = scoreGame(computerHand, dealerHand)
    if result == 1:
        print ("  Computer won.")
    else:
        print ("  Dealer won.")
    print ("")

# then, initialize the variables for the big run of sample games
print ("")
print ("Now, let me simulate %d games for you." % gamesTotal)

# the baseline variables
computerWins = 0
computerTies = 0
gamesPlayed = 0
decisions = 0
agree = 0
failedToTake = 0
failedToStand = 0

while gamesPlayed < gamesTotal:
    
    # no one has cards yet
    computerHand = []
    dealerHand = []
      
    # create a new 52-card deck
    deck = makeDeck(computerHand, dealerHand, not hidden)
    
    # give the computer one card
    takeCard = newCard(deck)
    computerHand.append(takeCard)
    deck[takeCard] -=1

    # give the dealer their revealed card
    takeCard = newCard(deck)
    dealerHand.append(takeCard)
    deck[takeCard] -=1

    # give the computer their second card
    takeCard = newCard(deck)
    computerHand.append(takeCard)
    deck[takeCard] -=1

    # give the dealer their secret card
    takeCard = newCard(deck)
    dealerHand.append(takeCard)
    deck[takeCard] -=1

    # let the computer play
    finished = False
    while not finished:
        
        # to evaluate our algorithm, count the number of decisions made
        decisions = decisions + 1
        
        if (findBestMove(computerHand, dealerHand) == TAKE):
            takeCard = newCard(deck)
            deck[takeCard] -= 1
            computerHand.append(takeCard)
        else:
            finished = True

        # check to see if we should stop
        if valueHand(computerHand) > 20:
            finished = True

    # dealer now can take more cards, up to 17        
    dealerHand = playTo17(computerHand, dealerHand, not hidden)

    # see who won
    result = scoreGame(computerHand, dealerHand)
    if result == 1:
        computerWins = computerWins + 1
    if result == 0:
        computerTies = computerTies + 1
        
    gamesPlayed = gamesPlayed + 1


# report summary statistics
computerLosses = gamesPlayed - computerWins - computerTies
print ("")
print ("Games played:    %5d" % gamesPlayed)
print ("Computer wins:   %5d" % computerWins)
print ("Computer losses: %5d" % computerLosses)
print ("Tie games:       %5d" % computerTies)
print ("")
