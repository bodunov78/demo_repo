from itertools import *

a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 0]
# region product
s = list(product(a, b, repeat=2))
# endregion

print(s)
print()
# region permutation перестановка
s = list(permutations(a))
print(s)
print()
# end region
# region combinations выборка 3 элементов из a
cnt = 0
for x in combinations(a, 3):
    cnt += 1
    print(x, cnt)

# end region
