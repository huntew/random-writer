######################################
# Random Writer programming assignment
# Hunter Montalvo & Julius Smith
# 2023-09-10
######################################

# import libraries
from random import randint, choice 


###########
# FUNCTIONS
###########
# returns a random seed of length level (or k) from the book
def get_seed():
    rand_i = randint(0, len(book) - level) # pick a random index that represents the beginning of the seed in the book
    seed = book[rand_i:rand_i+level] # choose a random seed to start with, from start to end - k length (bc if its past k length then theres nothing after)
    return seed, rand_i # return the random seed of length level (or k)
    
    
# returns a random next character given a seed from the book
def get_next_char(seed, level):
    i = 0  # initialize the current index (where we begin to look in the book
    char_list = []
    while i < len(book): # continually find the seed in the book
        
        seed_i = book.find(seed, i) # find the index of the seed in the book beginning at the current index
        
        if seed_i == -1 or seed_i + level >= (len(book) - 1): # abort if the seed is not found (or it's at the end of the book)
            break
        
        else: # otherwise, add the next character to the list
            char_list.append(book[seed_i + level])
            i = seed_i + 1 # and update the index in the book
            
    if len(char_list) >= 1:
        return choice(char_list) # if there is at least one next character in the list of characters, return a randomly chosen one
    else:
        return None # otherwise, return some appropriate trigger (e.g., None)       

######
# MAIN
######
# grab command line arguments (or manually set the parameters)
#  k (or level) -> the level of analysis performed on the book
#  length -> the length of output to generate
#  filename -> the filename that contains the text of the book

level = 5
length = 150
filename = "hg-wells_the-time-machine.txt"

# grab the book
with open(filename, "r") as f:
    book = f.read()

generated = '' # initialize the output

seed, rand_i = get_seed() # pick a random seed of length level (or k)
original_seed = seed # store original seed
times_generated = 0
while (len(generated) < length): # repeat as long as there isn't enough output yet
    
    char = get_next_char(seed, level) # get a random next character

    if char != None: # if one exists
        generated += char # add it to the output
        times_generated += 1
        new_seed = seed + char # placeholder to change seed, add the new character to the end of the current seed
        seed = new_seed[1:] # and recalculate the seed (the seed is shifted over the the right one, by starting at the index of the num of times a generation has happened
        
    else:
        seed, rand_i = get_seed() # otherwise, pick another random seed
print(original_seed + generated) # display the output
''# ask if we print the original chosen seed or only the generated content


