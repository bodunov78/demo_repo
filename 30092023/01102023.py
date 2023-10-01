# from itertools import *
# s = "ABCDEF"

# a = [x for x in product(s, repeat=7) if all(x.count(y) <= 3 for y in set(x))]
# a = [x for x in product(s, repeat=7)]
# b=list(map(a,"".join())

# m = [x for x in a if (all(x.count(y * x.count(y)) == 1 for y in set(x)))]
# m=list(map(lambda x: "".join(x),a))


a=[8,2,3,4,5,6]
# b=a
b=a[:]
a[1]=10
# del(a[0])
print(sorted(a),a,b)
a.sort(reverse=1)
print(a)