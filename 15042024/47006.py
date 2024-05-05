from itertools import *

cnt = 0
with open("47006.txt") as f:
    for s in f:
        m = list(map(int, s.split()))
        a = [list(x) for x in combinations(m, 3)]

        c = [(sum(x) - max(x) > max(x)) for x in a]
        if all(c):
            cnt += 1
            #SSS
    print(cnt)
