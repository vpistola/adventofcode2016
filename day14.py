# Day 14: One-time pad
# --------------------
#
#A hash is a key only if:
#
#It contains three of the same character in a row, like 777. Only consider the first such triplet #in a hash.
#One of the next 1000 hashes in the stream contains that same character five times in a row, like #77777.
#
#Given the actual salt in your puzzle input, what index produces your 64th one-time pad key?
    
import hashlib, re, time
from itertools import islice, count
from functools import lru_cache

salt = 'yjdafjpo'

#@lru_cache(1001)
#def hashval(i): return hashlib.md5(bytes(salt + str(i), 'utf-8')).hexdigest()

def is_key(num):
    "A key has a triple like '777', and then '77777' in one of the next thousand hashval(i)."
    three = re.search(r'(.)\1\1', hashval(num))
    if three:
        five = three.group(1) * 5
        for n in range(1, 1001):
            if re.search(five, hashval(num + n)): return True
    return False

# Part one
#print(next(islice(filter(is_key, count()), 63, None), None))


# Part two - different hashval (run md5 2016 times)
@lru_cache(1001)
def hashval(i, stretch=2016): 
    h = hashlib.md5(bytes(salt + str(i), 'utf-8')).hexdigest()
    for i in range(stretch):
        h = hashlib.md5(bytes(h, 'utf-8')).hexdigest()
    return h

t1 = time.time()    
print(next(islice(filter(is_key, count()), 63, None), None))    
t2 = time.time()
print("Time elapsed:", t2 - t1, "seconds")
#
    
    