from adx import *






























from adx import *
from itertools import *
def f(x, y, z, w):
   return ( (z==w) or (w and (not x)) or (x and (not y)))


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
   tab = [(0, a1, 0, 0), (0, a2, a3, 0), (0, a4, a5, a6)]
   if len(tab) == len(set(tab)):
      for p in permutations('xyzw'):
         if [f(**dict(zip(p, r))) for r in tab] == [0, 0, 0]:
            print(p)
