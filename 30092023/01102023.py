from itertools import *
s = "ABCDEF"

a = [x for x in product(s, repeat=7) if all(x.count(y) <= 3 for y in set(x))]
a = [x for x in product(s, repeat=7)]
# b=list(map(a,"".join())

# m = [x for x in a if (all(x.count(y * x.count(y)) == 1 for y in set(x)))]
m=list(map(lambda x: "".join(x),a))

print(m)