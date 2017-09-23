# DAY 11: Radioisotope Thermoelectric Generators
# ----------------------------------------------

from utilities import *
import time

State = namedtuple('State', 'elevator, floors')

#-------------------------------------------------------------------------------------------#
def astar_search(start, h_func):
    "Find a shortest sequence of states from start to a goal state (a state s with h_func(s) == 0). g is the path cost and h is the estimate of the distance from the goal state. The total cost is the f. At the goal state h = 0."
    
    frontier  = [(0, start)] # A priority queue, ordered by path length, f = g + h
    previous  = {start: None}  # start state has no previous state; other states will
    path_cost = {start: 0}     # The cost of the best path to a state.
    
    while frontier:
        (f, s) = heappop(frontier)
        if h_func(s) == 0:
            break
        
        floor, floors = s  # s: state
        combos = list(combinations(floors[floor], 1)) + list(combinations(floors[floor], 2)) 
        directions = [dir for dir in (1, -1) if 0 <= floor+dir < 4]
        #print(directions)
        for stuff in combos:
            for L2 in directions: 
                newfloors = list(floors)
                newfloors[floor] = tuple(x for x in floors[floor] if x not in stuff)
                newfloors[floor + L2] = tuple(sorted(floors[floor + L2] + stuff))
                if not legal_floor(newfloors[floor]) and not legal_floor(newfloors[floor + L2]):
                    continue
            
                next_state = State(floor+L2, tuple(newfloors))
                #print(next_state)
                new_cost = path_cost[s] + 1
                if next_state not in path_cost or new_cost < path_cost[next_state]:
                    path_cost[next_state] = new_cost
                    priotiry = new_cost - len(newfloors[3])*10  # alternative h_func
                    previous[next_state] = s
                    heappush(frontier, (priotiry, next_state))
                        
    return path_cost[s]
#-------------------------------------------------------------------------------------------#


#-------------------------------------------------------------------------------------------#
def legal_floor(floor):
    "Floor is legal if no RTG, or every chip has its corresponding RTG."
    rtgs  = any(r.endswith('G') for r in floor)
    chips = [c for c in floor if c.endswith('M')]
    return not rtgs or all(generator_for(c) in floor for c in chips)

def generator_for(chip): return chip[:2] + 'G'

def h_func(state):
    "An estimate of the number of moves needed to move everything to top."
    total = sum(len(floor) * i for (i, floor) in enumerate(reversed(state.floors)))
    return math.ceil(total / 2) # Can move two items in one move.
#-------------------------------------------------------------------------------------------#


''' 
# Answer [part-1]:
t1 = time.time()
#part1 = State(0, (fs('POG', 'THG', 'THM', 'PRG', 'RUG', 'RUM', 'COG', 'COM'), fs('POM', 'PRM'), Ø, Ø))
part1 = State(0, (
    tuple(sorted(('POG', 'THG', 'THM', 'PRG', 'RUG', 'RUM', 'COG', 'COM'))),
    tuple(sorted(('POM', 'PRM'))), (), ()
))
path1 = astar_search(part1, h_func, moves_func)
print(astar_search(part1, h_func))
t2 = time.time()
print("Time elapsed:", t2 - t1, "seconds")
'''


# Answer [part-2]:
t1 = time.time()
#part2 = State(0, (fs('POG', 'THG', 'THM', 'PRG', 'RUG', 'RUM', 'COG', 'COM','ELG','ELM','DIG','DIM'), fs('POM', 'PRM'), Ø, Ø))
part2 = State(0, (
    tuple(sorted(('POG', 'THG', 'THM', 'PRG', 'RUG', 'RUM', 'COG', 'COM','ELG','ELM','DIG','DIM'))),
    tuple(sorted(('POM', 'PRM'))), (), ()
))
print(astar_search(part2, h_func))
t2 = time.time()
print("Time elapsed:", t2 - t1, "seconds")

#  _   
# |_|