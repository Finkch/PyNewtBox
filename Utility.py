#   Contains functions that don't fit anywhere else
import os

#   Clears the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#   Rounds a number to a string of set size
#       That way, prints don't jumble around in their size
def round_str(num):
    return "{:.3e}".format(num)
