from itertools import *
from time import *

def fu1():
    s="ABCD"
    for x in combinations(s,3):
        print(*x,x)




ts=time()
fu1()
print(time()-ts)
