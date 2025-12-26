#100000 888888
s1="12345678"
s0="012345678"
from itertools import product
count = 0
for p in product(s0, repeat=6):
    p="".join(p)
    p = p.replace('3', '1').replace('5', '1').replace('7', '1')
    if p.count("4") == 1 and p[0]!="0" and p.count("1")==2:
        count+=1
print(count)
