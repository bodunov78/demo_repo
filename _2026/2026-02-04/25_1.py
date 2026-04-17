from time import *
from itertools import *
from math import *
ts=time()


def F(n):
    deliteli = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            deliteli |= {i, n // i}
    return sorted(deliteli)


for n in range(110_250_000, 110_300_000 + 1):
    deliteli = F(n)
    if len(deliteli) >= 2:
        M = deliteli[-1] + deliteli[-2]
        if M % 10000 == 1002:
            print(n)
print (time()-ts)