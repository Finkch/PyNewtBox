#   Contains functions that don't fit anywhere else
import os

#   Clears the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
