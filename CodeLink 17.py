# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 17
# Imitation
# last revised 4/28/26

# There are countless ways to build an imitation engine using the ideas from
# Chapter Ten. I suggest starting with something simple that is easy to debug,
# and then later adding more complicated details.  For instance, maybe start
# by searching the sample text to identify every unique 4-character phrase.
# Then, for each phrase, take note of what characters come next, and how often.
# Using that information, you can generate text that follows similar patterns.
#
# In that same spirit, use simple sample text at first.  Once your code is working,
# then you can bring Taylor Swift and William Shakespeare into the mix.
#

import random

def makeChain (sample, chainLength):

    # Use this function to build a chain based on some sample text.

    # One approach is create one link for every unique phrase found in the text.
    # For example, suppose you are building 4-character phrases.  One link might
    # be the 4 characters "c-o-n-s" and that link would then note that,
    # after "cons", we sometimes have letter 't' ("construct", "constant"), we sometimes
    # have letter 'i' ("consider"), and so on.  Another link might then focus on the
    # 4 characters "o-n-s-t" and record that, after "onst", we somtimes have the
    # letter 'a' ("constant"), sometimes the letter 'r' ("construct"), etc.

    chain = []

    print("This needs to be implemented!")

    return chain
        


def talk (chain, phrase, chain_length):

    lettersUsed = 0

    # start with a phrase that is in the sample
    print(phrase, end="")

    while lettersUsed < 1000:

        # find the phrase in the chain, then choose from the options!
        print("Needs to be implemented")


# main program
# ############

# Use simple sample text for now, so that you can easily debug.
# Later, you can add more complicated, longer samples like Taylor Swift lyrics or Shakespeare.

sample = "This dog. This cat. This dog. This horse. This dog. This mouse. This dog. This rat. This dog."

# When you are ready to add longer text, paste that text into a file named "sample.txt" in the same folder
# as this Python code, and then uncomment the below two lines of code. The code will then access your file
# and copy your text into the 'sample' variable.

# with open('sample.txt', 'r') as file:
#    sample = file.read()

# define variables
trainedChain = []

# ask the user how many characters to use in each link
# when debugging, start with 4, and then think about whether to move to 1 or 2 or even 10

chainLength = int(input("How long do you want the chain? "))
trainedChain = makeChain(sample, chainLength)

print("Made chain!")
print()

# we are now ready to generate some text
# the second argument below is just the first 'chainLength' number of characters from the original sample
talk(trainedChain, sample[:chainLength], chainLength)
print(" ... Enough.")

print()
print()
