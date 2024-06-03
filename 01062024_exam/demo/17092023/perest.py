a = ['A', 'B', 'C', 'D', '5']

# получить перестановки из массива a = [1, 2, 3, 4, 5]
s = [x for x in range(10000, 100000) if all(str(x).count(str(y)) == 1 for y in a)]

print(s, len(s))

# получить все комбинации из массива a = [1, 2, 3, 4, 5]
s = [x for x in range(10000, 100000) if all(a.count(int(z)) > 0 for z in str(x))]

print(s, len(s))
k = 9
num = 0
print(str(num).rjust(6, '0'))

# достроить нули до строчки длиной 7
kk = '0' * (k - len(str(num))) + str(num)
print(kk)
print(str(num).rjust(6, '0'))

for i in range(5 ** 5):
    s = ""
    j = i
    while j > 0:
        ost = j % 5
        j = j // 5
        s = str(ost) + s
    l = s.rjust(5, "0")
    w = ""
    for z in l:
        w += a[int(z)]
    print(w)

m = [str(x) + str(y) + str(z) for x in range(4) for y in range(4) for z in range(4) if
     len(str(x) + str(y) + str(z)) == len(set(str(x) + str(y) + str(z)))]
print(m)
