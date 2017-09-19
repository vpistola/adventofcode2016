'''
Day 10: Balance Bots

In this puzzle, a fleet of robots exchange some chips from input bins, passing them among themselves, and eventually putting them in output bins. We are given instructions like this:

	value 5 goes to bot 2
	bot 2 gives low to bot 1 and high to bot 0
	value 3 goes to bot 1
	bot 1 gives low to output 1 and high to bot 0
	bot 0 gives low to output 2 and high to output 0
	value 2 goes to bot 2

'''
from utilities import *

def bots(instructions, goal={17, 61}):
    "Follow the data flow instructions, and if a bot gets the goal, print it."
    def give(giver, chip, recip):
        "Pass the chip from giver to recipient."
        has[giver].discard(chip)
        has[recip].add(chip)
        chips = has[recip]
        if chips == goal:
            print(recip, 'has', goal)
        if len(chips) == 2:
            give(recip, min(chips), gives[recip][0])
            give(recip, max(chips), gives[recip][1])
            
    has   = defaultdict(set)       # who has what
    gives = {giver: (dest1, dest2) # who will give what
             for (giver, dest1, dest2) 
             in re.findall(r'(bot \d+) gives low to (\w+ \d+) and high to (\w+ \d+)', instructions)}
    for (chip, recip) in re.findall(r'value (\d+) goes to (\w+ \d+)', instructions):
        give('input bin', int(chip), recip)
    return has

has = bots(Input(10).read())
print( has['output 0'].pop() * has['output 1'].pop() * has['output 2'].pop() )

# END