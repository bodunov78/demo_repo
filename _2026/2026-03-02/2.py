from itertools import *

for x in product("ABC", repeat=4):
    print (x)

for x in combinations("ABC", 3):
    print (x)

for x in permutations("ABC",3):
    print (x)