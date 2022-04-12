#   Contains functions that don't fit anywhere else
import os

#   Clears the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#   Rounds a number to a string of set size
#       That way, prints don't jumble around in their size
def round_str(num):
    return "{: .3e}".format(num)

#   Converts a number to
def seconds_to_clock(seconds):
    return "{yyyy:02}-{mm:02}-{dd:02}, {hh:02}:{mi:02}:{ss:02}".format(yyyy = seconds // 31104000 + 1, mm = seconds // 2592000 % 12 + 1, dd = seconds // 86400 % 30 + 1, hh = seconds // 3600 % 24, mi = seconds // 60 % 60, ss = seconds % 60)

