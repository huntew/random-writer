######################################
# Random Writer programming assignment
# Hunter Montalvo & _______
# 2023-09-08
######################################

# import libraries
from random import randint, choice

###########
# FUNCTIONS
###########
# returns a random seed of length level (or k) from the book
def get_seed():
    # pick a random index that represents the beginning of the seed in the book
    k = int(input("k level: "))
    while k < 0: # if input is negative
        k = int(input("k level: ")) # keep asking until it's positive
    # return the random seed of length level (or k)
    return k
    
# returns a random next character given a seed from the book
def get_next_char():
    def __init__(self, i):
        self._c = []  # initialize the list of characters
        self._i = i   # initialize the current index (where we begin to look in the book)

   
    # continually find the seed in the book
        # find the index of the seed in the book beginning at the current index

        # abort if the seed is not found (or it's at the end of the book)

        # otherwise, add the next character to the list

        # and update the index in the book

    # if there is at least one next character in the list of characters, return a randomly chosen one

    # otherwise, return some appropriate trigger (e.g., None)

######
# MAIN
######
# grab command line arguments (or manually set the parameters)
#  k (or level) -> the level of analysis performed on the book
#  length -> the length of output to generate
#  filename -> the filename that contains the text of the book
level = 1
length = 150
filename = "hg-wells_the-time-machine.txt"

# grab the book
with open(filename, "r") as f:
    book = f.read()

# initialize the output

# pick a random seed of length level (or k)
get_seed()
# repeat as long as there isn't enough output yet
    # get a random next character

    # if one exists
        # add it to the output

        # and recalculate the seed

    # otherwise, pick another random seed

# display the output

