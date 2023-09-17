a = [1, 2, 3, 4, 5]

s = [x for x in range(10000, 100000) if all(str(x).count(str(y)) == 1 for y in a)]

print(s, len(s))

s = [x for x in range(10000, 100000) if all(a.count(int(z)) > 0 for z in str(x))]

print(s, len(s))
k = 6
num = 0
print(str(num).rjust(6, '0'))
