from itertools import *
from adx import *
from csv import *


def f(x,y,a):
    return ((x < a)or (y<a)or (x+3*y >180))


for a in range(200):
    k=1
    for x in range(500):
        for y in range(500):
            if not f(x,y,a):
                k=0
                break
    if k==1:
        print(a)
        break



