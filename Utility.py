#   Contains functions that don't fit anywhere else
import os

#   Clears the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#   Rounds a number to a string of set size
#       That way, prints don't jumble around in their size
def round_str(num):
    return "{: .3e}".format(num)

#   Converts a number to clock formatted string
#       Rounds the seconds downward
def seconds_to_clock(seconds):
    return "{yyyy:02}-{mm:02}-{dd:02}, {hh:02}:{mi:02}:{ss:02}".format(yyyy = int(seconds // 31104000 + 1), mm = int(seconds // 2592000 % 12 + 1), dd = int(seconds // 86400 % 30 + 1), hh = int(seconds // 3600 % 24), mi = int(seconds // 60 % 60), ss = int(seconds % 60))

