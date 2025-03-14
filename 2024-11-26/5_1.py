#18274
from itertools import *
for s in product("12",repeat=5):
    d=5
    for c in s:
        if c=='2':
            d=d*2
        else:
            d=d+3
    if d==76:
        print (s[::-1])

        