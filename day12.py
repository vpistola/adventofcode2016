# DAY 12: Leonardo's Monorail
# ---------------------------

from utilities import *

#regs = dict(a=0, b=0, c=0, d=0)     # part1
regs = dict(a=0, b=0, c=1, d=0)     # part2

def parse(line): 
    "Split line into words, and convert to int where appropriate."
    return tuple((x if x.isalpha() else int(x)) 
                 for x in line.split())

code = [parse(line) for line in Input(12)]

def val(x): return (regs[x] if x in regs else x)

i = 0
while i < len(code):
    inst = code[i]
    op, x, y = inst[0], inst[1], inst[-1]
    i += 1
    if   op == 'cpy': regs[y] = val(x)
    elif op == 'inc': regs[x] += 1
    elif op == 'dec': regs[x] -= 1
    elif op == 'jnz' and val(x): i += y - 1   

print(code)
