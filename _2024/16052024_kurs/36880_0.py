from math import *


for m in range(0,31,2):
    for n in range(1, 20, 2):
        N=(2**m)*(3**n)
        if  400_000_000<=N<=600_000_000:
            print (N)
