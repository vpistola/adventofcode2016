# DAY 13: A Maze of Twisty Little Cubicles
# ----------------------------------------
#
# Find x*x + 3*x + 2*x*y + y + y*y.
# Add the office designer's favorite number (your puzzle input).
# Find the binary representation of that sum; count the number of bits that are 1.
#    If the number of bits that are 1 is even, it's an open space.
#    If the number of bits that are 1 is odd, it's a wall.

import heapq, time
from collections import deque

favorite = 1352
goal = (31, 39)
w = 50
h = 50
start = (1,1)

def build_map():
    matrix = [ [0 for x in range(w)] for y in range(h)]
    for x in range(w):
        for y in range(h):
            #print(x,y)
            num = x*x + 3*x + 2*x*y + y + y*y + favorite
            one_bits = bin(num).count("1")
            if one_bits % 2 == 0:
                matrix[x][y] = '.'
            else:
                matrix[x][y] = '#'
    return matrix
    
matrix = build_map()
#print(matrix)

def neighbors(point): 
    "The four neighbors of a given point (without diagonals)."
    x, y = point
    return ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
    
def traverse_matrix(matrix, goal):
    "This is the a* graph search algorithm."
    frontier = []
    heapq.heappush(frontier, (0, start))
    cost_so_far = {start: 0}
    
    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal:
            break
        for s in neighbors(current):
            if matrix[s[0]][s[1]] == '.':
                next = (s[0], s[1])
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    #abs(x2 - x1) + abs(y2 - y1), between two points (x1, y1) and (x2, y2)
                    priority = abs(next[0] + current[0]) + abs(next[1] + current[1])
                    heapq.heappush(frontier, (priority, next))
            else: continue
            
    return cost_so_far[current]

# Part one
#t1 = time.time()
#print(traverse_matrix(matrix, goal))     
#t2 = time.time()    
#print("Time elapsed:", t2 - t1, "seconds")    


# Part Two
# How many locations (distinct x,y coordinates, including your starting location) can you reach # in at most 50 steps?
    
def counting_states(matrix, start, goal):
    "Count how many locations can you reach in at most 50 steps."
    frontier = deque([start])
    explored = {start: 1}    # the previous states
    while frontier:
        current = frontier.popleft()
        if explored[current] < goal:
            for s in neighbors(current):
                if matrix[s[0]][s[1]] == '.' and s not in explored:
                    frontier.append(s)
                    explored[s] = explored[current] + 1
    return len(explored)

print(counting_states(matrix, start, 50))
    
# END