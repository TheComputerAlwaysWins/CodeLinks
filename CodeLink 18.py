# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 18
# Black Boxes
# last revised 4/29/26

# This is a full implementation of the black box strategy developed
# in Chapter Eleven.  Note that a fully random approach would get half
# the examples right.  This simple neural network exceeds that baseline
# even before we do much fine-tuning or add much complexity.

# ERRATA
# Note that there is an error in the code on line 166 on page 143 of the book.
# The code there should refer to gameData[0], which is the correct label for this player.
# In the book, we accidentally refer to gameData[9], which is the player's ninth game.
# Thanks to readers for catching that mistake.

# The 4/29/26 revision also:
# . . . improves the makeRandom() and makeReluctant() functions, to increase clarity on the gameData variable
# . . . increases the number of sample players in the training set
# . . . increases the number of times the computer is allowed to try new weights, looking to reduce network error
# . . . reports more informative statistics about how the network performs

import random
import math

# function defintions
# ###################

def smush(value):
    # the mathematical smush function
    
    sigmoid = 1/(1+math.e**(-value))        
    return sigmoid


def makeRandom():
    # generate 9 random games

    sample = []

    # label the games as random
    sample.append(0)

    # generate data consistent with a random player    
    for counter in range(9):
        sample.append(random.randint(1,3))

    return sample


def makeReluctant():
    # generate 9 games, with some reluctance

    sample = []

    # label the games as reluctant
    sample.append(1)

    # generate data consistent with a reluctant player
    
    # their first game is random
    sample.append(random.randint(1,3))

    # their remaining games are random, but repeats are discouraged
    for counter in range (1,9):
        sample.append(random.randint(1,3))
        if sample[counter] == sample[counter-1]:
            sample[counter] = random.randint(1,3)
    
    return sample


def nicePrint(array):
    for counter in range(len(array)):
        print(array[counter])
    print("")


def crazyMath(gameData,a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,output):
            
    # calculate the A values, using the current games and weights
    a1[10] = smush(a1[1]*gameData[1] + a1[2]*gameData[2] + a1[3]*gameData[3] + a1[4]*gameData[4] + a1[5]*gameData[5] + a1[6]*gameData[6] + a1[7]*gameData[7] + a1[8]*gameData[8] + a1[9]*gameData[9])
    a2[10] = smush(a2[1]*gameData[1] + a2[2]*gameData[2] + a2[3]*gameData[3] + a2[4]*gameData[4] + a2[5]*gameData[5] + a2[6]*gameData[6] + a2[7]*gameData[7] + a2[8]*gameData[8] + a2[9]*gameData[9])
    a3[10] = smush(a3[1]*gameData[1] + a3[2]*gameData[2] + a3[3]*gameData[3] + a3[4]*gameData[4] + a3[5]*gameData[5] + a3[6]*gameData[6] + a3[7]*gameData[7] + a3[8]*gameData[8] + a3[9]*gameData[9])
    a4[10] = smush(a4[1]*gameData[1] + a4[2]*gameData[2] + a4[3]*gameData[3] + a4[4]*gameData[4] + a4[5]*gameData[5] + a4[6]*gameData[6] + a4[7]*gameData[7] + a4[8]*gameData[8] + a4[9]*gameData[9])
    a5[10] = smush(a5[1]*gameData[1] + a5[2]*gameData[2] + a5[3]*gameData[3] + a5[4]*gameData[4] + a5[5]*gameData[5] + a5[6]*gameData[6] + a5[7]*gameData[7] + a5[8]*gameData[8] + a5[9]*gameData[9])

    # calculate the downstream B values, using the A values and weights
    b1[6] = smush(b1[1]*a1[10] + b1[2]*a2[10] + b1[3]*a3[10] + b1[4]*a4[10] + b1[5]*a5[10])
    b2[6] = smush(b2[1]*a1[10] + b2[2]*a2[10] + b2[3]*a3[10] + b2[4]*a4[10] + b2[5]*a5[10])
    b3[6] = smush(b3[1]*a1[10] + b3[2]*a2[10] + b3[3]*a3[10] + b3[4]*a4[10] + b3[5]*a5[10])
    b4[6] = smush(b4[1]*a1[10] + b4[2]*a2[10] + b4[3]*a3[10] + b4[4]*a4[10] + b4[5]*a5[10])
    b5[6] = smush(b5[1]*a1[10] + b5[2]*a2[10] + b5[3]*a3[10] + b5[4]*a4[10] + b5[5]*a5[10])

    # and lastly calculate the downstream output prediction, using the B values and weights
    output[6] = smush(output[1]*b1[6] + output[2]*b2[6] + output[3]*b3[6] + output[4]*b4[6] + output[5]*b5[6])


# main program
# ############

print ("")
print ("I am generating some training data.")

# create 50 fictional players of each type
samplesPerType = 50

# store each player as an entry in testData
testData = []

# do not use testData[0], so samples are labeled as sample 1, sample 2, ... sample 2*samplesPerType
testData.append([0,0,0,0,0,0,0,0,0,0])

for example in range(samplesPerType):    
    testData.append(makeRandom())
    testData.append(makeReluctant())

# STEP 1: establish the key variables

# the sample we are evaluating
gameData = [0,0,0,0,0,0,0,0,0,0]

# the A nodes, not actually using A[0]
A1 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
A2 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
A3 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
A4 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
A5 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

# the B nodes, not actually using B[0]
B1 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
B2 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
B3 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
B4 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
B5 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

# the output node, not actually using output[0]
output = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

# likewise, for the second network, AA nodes
AA1 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
AA2 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
AA3 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
AA4 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
AA5 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

# and BB nodes
BB1 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
BB2 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
BB3 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
BB4 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
BB5 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

# and lastly, the otherOutput node
otherOutput = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]


# STEP 2: randomly initialize the weights

for counter in range(1,10):
    A1[counter] = (random.random()-0.5)
    A2[counter] = (random.random()-0.5)
    A3[counter] = (random.random()-0.5)
    A4[counter] = (random.random()-0.5)
    A5[counter] = (random.random()-0.5)
    
for counter in range(1,6):
    B1[counter] = (random.random()-0.5)
    B2[counter] = (random.random()-0.5)
    B3[counter] = (random.random()-0.5)
    B4[counter] = (random.random()-0.5)
    B5[counter] = (random.random()-0.5)
    
for counter in range(1,6):
    output[counter] = (random.random()-0.5)
    

# STEP 3: the loop

print ("I am now ready to use that data to build my network.")
print ("I might need a few minutes to work on this.")

# stop conditions
satisfied = False
attempts = 0

while not satisfied:

    # try the current pattern of coefficients
    totalError = 0.0
    sample = 1
  
    while sample <= 2*samplesPerType:
        
        #load the new sample
        for counter in range(10):
            gameData[counter] = testData[sample][counter]
        
        # run the Crazy Math
        crazyMath(gameData,A1,A2,A3,A4,A5,B1,B2,B3,B4,B5,output)
        
        # update the error measurement by comparing label to network output
        totalError = totalError + (gameData[0]-output[6])**2
        
        # go back for our next sample
        sample = sample + 1
        
    # now change the coefficients a little, and test that second version
    # note that the expression below moves each value +/- 0.05
    # the random.random() function results in a number from 0 to 1;
    # subtracting 0.5 gives a number from -0.5 to +0.5
    # multiplying by 2 gives a number from -1 to 1
    # and multiplying by 0.05 gives the final range: -0.05 to + 0.05
      
    for counter in range(1,10):
        AA1[counter] = A1[counter] + 0.05 * 2 * (random.random()-0.5)
        AA2[counter] = A2[counter] + 0.05 * 2 * (random.random()-0.5)
        AA3[counter] = A3[counter] + 0.05 * 2 * (random.random()-0.5)
        AA4[counter] = A4[counter] + 0.05 * 2 * (random.random()-0.5)
        AA5[counter] = A5[counter] + 0.05 * 2 * (random.random()-0.5)
        
    for counter in range(1,6):
        BB1[counter] = B1[counter] + 0.05 * 2 * (random.random()-0.5)
        BB2[counter] = B2[counter] + 0.05 * 2 * (random.random()-0.5)
        BB3[counter] = B3[counter] + 0.05 * 2 * (random.random()-0.5)
        BB4[counter] = B4[counter] + 0.05 * 2 * (random.random()-0.5)
        BB5[counter] = B5[counter] + 0.05 * 2 * (random.random()-0.5)
        
    for counter in range(1,6):
        otherOutput[counter] = output[counter] + 0.05 * 2 * (random.random()-0.5)
        
    # and examine the training data using these new coefficients
    otherError = 0.0
    sample = 1
    
    while sample <= 2*samplesPerType:
        
        #load the next sample
        for counter in range(10):
            gameData[counter] = testData[sample][counter]
       
        # run the Crazy Math
        crazyMath(gameData,AA1,AA2,AA3,AA4,AA5,BB1,BB2,BB3,BB4,BB5,otherOutput)
        
        # caculate the new error
        otherError = otherError + (gameData[0]-otherOutput[6])**2
 
        # go back for our next sample
        sample = sample + 1

   
    if totalError > otherError:
        # start using the new coefficients
        
        for counter in range(1,11):
            A1[counter] = AA1[counter]
            A2[counter] = AA2[counter]
            A3[counter] = AA3[counter]
            A4[counter] = AA4[counter]
            A5[counter] = AA5[counter]
            
        for counter in range(1,7):
            B1[counter] = BB1[counter]
            B2[counter] = BB2[counter]
            B3[counter] = BB3[counter]
            B4[counter] = BB4[counter]
            B5[counter] = BB5[counter]

        for counter in range(1,7):
            output[counter] = otherOutput[counter]
            
    if totalError < 0.1:
        # stop due to high accuracy
        # this will likely never happen in such a simple neural network
        satisfied = True
  
    if attempts > 50000:
        # after this many passes, stop due to lack of progress
        satisfied = True
        
    attempts = attempts + 1


print ("")
print ("Network is built.")
print ("Error measurement: %2.2f." % totalError)
print ("")
print ("To test the network, I will now run 1,000 sample players through the network.")
print ("I will keep track of whether I identify them correctly.")
print ("")

correct = 0

for counter in range(1000):

    newPlayer = random.randint(0,1)

    if newPlayer == 1:
        gameData = makeReluctant()
    else:
        gameData = makeRandom()

    # run the Crazy Math
    crazyMath(gameData,A1,A2,A3,A4,A5,B1,B2,B3,B4,B5,output)

    # how did I do?
    if (newPlayer == 0 and output[6]<=0.5):
        correct = correct + 1
    if (newPlayer == 1 and output[6]>0.5):
        correct = correct + 1        

print ("RESULTS: I correctly predicted %2d percent of the test cases." % (100*correct/1000))
print ("")    
