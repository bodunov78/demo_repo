from itertools import *
s="ABCD"
for x in product(s,repeat=4):
    print (x)

for x in combinations(s,3):
    print (x)
print ("permutation")
for x in permutations(s,3):
    print (x)