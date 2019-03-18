#########################################################################
#imports
import random
#########################################################################
#Functions
def roll_stats():
    rolls = []
    num = 0
    for x in range(4):
        rolls.append(random.randint(1,6))
    rolls.sort()
    rolls.reverse()
    for x in range(3):
        num += rolls[x]
    return num
