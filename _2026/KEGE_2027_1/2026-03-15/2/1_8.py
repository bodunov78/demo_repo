from itertools import *
# for a1,a2,a3,a4,a5,a6,a7 in product([0,1],repeat=7):
#     tab = [(a1, a2, 1, a3), (a4, 1, 0, a5), (1, 0, a6, a7)]
#     print (tab)
for p in permutations('xyzw'):
    print (p)