#Тип 27 № 38604
f = open("27-B.txt")
n = int(f.readline())
mins = [1000000001 for i in range(43)]
minl = [0 for i in range(43)]
sum = 0
maxsum = 0
minlen = 0
ms = 0
l = 0
for i in range(1, n + 1):
    num = int(f.readline())
    sum = sum + num
    d = sum % 43
    if d == 0:
        maxsum = sum
        minlen = i
    else:
        ms = sum - mins[d]
        l = i - minl[d]
        if ms > maxsum:
            maxsum = ms
            minlen = l
        if (ms == maxsum) and (l < minlen):
            maxsum = ms
            minlen = l
        if sum < mins[d]:
            mins[d] = sum
            minl[d] = i
print(minlen)

#Тип 27 № 47231
from math import ceil
f = open("27-B.txt")

n = int(f.readline())
elems = []
sum = 0
rightSum = 0
leftSum = 0
for i in range(0, n):
    a, b = map(int, f.readline().split())
    elems.append([a, ceil(b / 36)])
cost = [0] * n
for i in range(1, n):
    cost[0] += (elems[i][0] - elems[0][0]) * elems[i][1]
    rightSum += elems[i][1]
for i in range(1, n):
    leftSum += elems[i - 1][1]
    cost[i] = cost[i - 1] - rightSum * (elems[i][0] - elems[i - 1][0]) + leftSum * (elems[i][0] - elems[i - 1][0])
    rightSum -= elems[i][1]
print(min(cost))


##Тип 27 № 36001
f = open("27-B.txt")
n = int(f.readline())
sum0 = 0
sum1 = 0
min1 = 20001
min2 = 20001
min3 = 20001
for i in f:
    x, y = i.split()
    x = int(x)
    y = int(y)
    if x % 2 == 1:
        if x > y:
            sum1 = sum1 + x
            sum0 = sum0 + y
            if (x % 2 == 1) and (y % 2 == 1) and ((x + y) < min1):
                    min1 = x + y
            if (x % 2 == 0) and (y % 2 == 1) and ((x + y) < min2):
                    min2 = x + y
            if (x % 2 == 1) and (y % 2 == 0) and ((x + y) < min3):
                    min3 = x + y
        else:
            sum1 = sum1 + y
            sum0 = sum0 + x
            if (x % 2 == 1) and (y % 2 == 1) and ((x + y) < min1):
                min1 = x + y
            if (y % 2 == 0) and (x % 2 == 1) and ((x + y) < min2):
                    min2 = x + y
            if (y % 2 == 1) and (x % 2 == 0) and ((x + y) < min3):
                    min3 = x + y
if (sum0 % 2 == 0) and (sum1 % 2 == 1):
    print(sum0 + sum1)
elif (sum0 % 2 == 1) and (sum1 % 2 == 0):
    if min1 < min2 + min3:
        print(sum0 + sum1 - min1)
    else:
        print(sum0 + sum1 - min2 - min3)
elif (sum0 % 2 == 1) and (sum1 % 2 == 1):
    if min2 < min3 + min1:
        print(sum0 + sum1 - min2)
    else:
        print(sum0 + sum1 - min3 - min1)
elif (sum0 % 2 == 0) and (sum1 % 2 == 0):
    if min3 < min2 + min1:
        print(sum0 + sum1 - min3)
    else:
        print(sum0 + sum1 - min2 - min1)


##Тип 27 № 45261
f = open("27-B.txt")
n = int(f.readline())
elems = [0 for i in range(n)]
answers = [0 for i in range(n)]
sum = 0
rightSum = 0
leftSum = 0
for i in range(0, n):
    elems[i] = int(f.readline())
for i in range(0, n):
    elems[i] = elems[i] * 3
for i in range(1, n // 2):
    sum = sum + elems[i] * i + elems[n - i] * i
    rightSum = rightSum + elems[i]
    leftSum = leftSum + elems[n - i]
sum = sum + elems[n // 2] * n // 2
answers[0] = sum
for i in range(1, n):
    answers[i] = answers[i - 1] + leftSum + elems[i - 1] - rightSum - elems[(i + (n // 2) - 1) % n]
    rightSum = rightSum - elems[i] + elems[(i + (n // 2) - 1) % n]
    leftSum = leftSum - elems[(i + (n // 2)) % n] + elems[i - 1]
print(min(answers))

##Тип 27 № 37162

f = open("27-B.txt")
k, s = 89, 0

mins = {0: (0, 0)}

res = []

for i in range(1, int(f.readline())+1):
    s += int(f.readline())
    if s % k in mins:
        res += [(s - mins[s % k][0], mins[s % k][1] – i)]

    else:
        mins[s % k] = (s, i)

print(-max(res)[1])

###ch_sum

f = open("27-B.txt")
n = int(f.readline())
k = 89
r = {0: (0, 0)}
ms = 0
m = float('inf')
for _ in range(n):
    x = int(f.readline())
    t = {}
    for key in r:
        t[(key + x) % k] = (r[key][0] + x, r[key][1] + 1)
    if x % k not in t:
        t[x % k] = (x, 1)
        r = t.copy()
    if 0 in r:
        if ms < r[0][0]:
        ms = r[0][0]
        m = r[0][1]
    elif ms == r[0][0]:
        m = min(t[0][1], m)
print(m)


## Тип 27 № 41002

f = open("27-B.txt")
n = int(f.readline())
lefts = [0 for i in range(30)]
maxsum = 0
for i in range(30):
    lefts[i] = 2 * 1000000000
    count = 0
    sum = 0
for i in range(1, n + 1):
    num = int(f.readline())
    sum = sum + num
    if (num % 2 == 1) and (num > 0):
        count = count + 1
    d = count % 30
    if sum < lefts[d]:
        lefts[d] = sum
    maxsum = max(maxsum, sum - lefts[d])
print(maxsum)

##Тип 27 № 33497

f = open("27-B.txt")
m = list(map(str, f.readlines()))
n = int(m[0])
mx = []
rez = 10 * 10
k = 0
for i in range(1, n + 1):
    x, y, z = (map(int, m[i].split()))
    mx.append(min(x, y, z))
    a = max(x, y, z)
    c = min(x, y, z)
    b = x + y + z - c - a
    if (a + b) % 2 != 0:
        k += 1
        if (a + c) % 2 != 0:
            rez = min(rez, abs(a - c))
        else:
            rez = min(rez, abs(a - b))

if k % 2 != 0:
    print(sum(mx))
else:
    print(sum(mx) + rez)

##Тип 27 № 33199

f = open("27-B.txt")
n = int(f.readline())
sum_a = sum_b = sum_max = 0
min_razn = 100000000
for i in range(n):
    a, b, c = map(int, f.readline().split())
    sum_max += max(a, b, c)
    sum_a += min(a, b, c)
    average = a + b + c - max(a, b, c) - min(a, b, c)
    sum_b += average
    if max(a, b, c) - average < min_razn and max(a, b, c) - average != 0 and max(a, b, c) - average % 2 != 0:
        min_razn = max(a, b, c) - average
if (sum_b % 2) == (sum_a % 2): print(sum_max - min_razn)
else: print(sum_max)

##Тип 27 № 38961

f = open("27-B.txt")
n = int(f.readline())
lefts = [0 for i in range(10)]
rights = [0 for i in range(10)]
for i in range(10):
    lefts[i] = 0
    rights[i] = 0
count = 0
sum = 0
for i in range(1, n + 1):
    num = int(f.readline())
    sum = sum + num
    if num % 2 == 0:
        count = count + 1
    d = count % 10
    if lefts[d] == 0:
        lefts[d] = sum
    rights[d] = sum
maxsum = 0
if count % 10 == 0:
    print(sum)
else:
    for i in range(1, count % 10 + 1):
        if (rights[i] - lefts[i]) > maxsum:
            maxsum = rights[i] - lefts[i]
if rights[0] > maxsum:
    maxsum = rights[0]
print(maxsum)

##Тип 27 № 29675

f = open("27-B.txt")
s = f.readlines()
n = int(s[0])
sum = 0
dif1 = 20001
dif2 = 20001
dif3 = 20001
dif4 = 20001
for i in range(1, n + 1):
    x, y = map(int, s[i].split())
    if x > y: sum += y
    else: sum += x
    if (abs(x-y) % 3 == 1) and (abs(x-y) < dif1):
        dif2 = dif1
        dif1 = abs(x - y)
    elif (abs(x-y) % 3 == 1) and (abs(x-y) < dif2): dif2 = abs(x-y)
    elif (abs(x-y) % 3 == 2) and (abs(x-y) < dif3):
        dif4 = dif3
        dif3 = abs(x - y)
    elif (abs(x-y) % 3 == 2) and (abs(x-y) < dif4): dif4 = abs(x-y)
if sum % 3 == 0:
    print(sum)
elif sum % 3 == 1:
    if (sum + dif3) < (sum + dif1 + dif2):
        print(sum + dif3)
    else: print(sum + dif1 + dif2)
elif sum % 3 == 2:
    if ((sum + dif1) < (sum + dif3 + dif4)):
        print(sum + dif1)
    else:
        print(sum + dif3 + dif4)


##Тип 27 № 35916

f = open("27-B.txt")
s = f.readlines()
n = int(s[0])
m0 = [1 for i in range(4)]
m1 = [1 for i in range(4)]
m2 = [1 for i in range(4)]
for i in range(1, 4):
    m0[i] = 100000000
    m1[i] = 100000000
    m2[i] = 100000000
for i in range(1, n + 1):
    x = int(s[i])
    if x % 3 == 0:
        if x < m0[1]:
            m0[3] = m0[2]
            m0[2] = m0[1]
            m0[1] = x
        elif x < m0[2]:
            m0[3] = m0[2]
            m0[2] = x
        elif x > m0[3]: m0[3] = x
    elif x % 3 == 1:
        if x < m1[1]:
            m1[3] = m1[2]
            m1[2] = m1[1]
            m1[1] = x
        elif x < m1[2]:
            m1[3] = m1[2]
            m1[2] = x
        elif x < m1[3]: m1[3] = x
    elif x % 3 == 2:
        if x < m2[1]:
            m2[3] = m2[2]
            m2[2] = m2[1]
            m2[1] = x
        elif x < m2[2]:
            m2[3] = m2[2]
            m2[2] = x
        elif x > m2[3]: m2[3] = x
sum0 = m0[1] + m0[2] + m0[3]
sum1 = m1[1] + m1[2] + m1[3]
sum2 = m2[1] + m2[2] + m2[3]
sum12 = m0[1] + m1[1] + m2[1]
if (sum0 < sum1) and (sum0 < sum2) and (sum0 < sum12): print(sum0)
elif (sum1 < sum0) and (sum1 < sum2) and (sum1 < sum12): print(sum1)
elif (sum2 < sum1) and (sum2 < sum0) and (sum2 < sum12): print(sum2)
else: print(sum12)

##Тип 27 № 36882

f = open("27-B.txt")
n = int(f.readline())
sum0 = 0
sum1 = 0
min1 = 20001
min2 = 20001
min3 = 20001
for i in f:
    x, y = i.split()
    x = int(x)
    y = int(y)
    if y % 2 == 1:
        if x > y:
            sum1 = sum1 + y
            sum0 = sum0 + x
            if (y % 2 == 1) and (x % 2 == 1) and ((x + y) < min1):
                    min1 = x + y
            if (y % 2 == 0) and (x % 2 == 1) and ((x + y) < min2):
                    min2 = x + y
            if (y % 2 == 1) and (x % 2 == 0) and ((x + y) < min3):
                    min3 = x + y
        else:
            sum1 = sum1 + x
            sum0 = sum0 + y
            if (y % 2 == 1) and (x % 2 == 1) and ((x + y) < min1):
                min1 = x + y
            if (x % 2 == 0) and (y % 2 == 1) and ((x + y) < min2):
                    min2 = x + y
            if (x % 2 == 1) and (y % 2 == 0) and ((x + y) < min3):
                    min3 = x + y
if (sum0 % 2 == 0) and (sum1 % 2 == 1):
    print(sum0 + sum1)
elif (sum0 % 2 == 1) and (sum1 % 2 == 0):
    if min1 < min2 + min3:
        print(sum0 + sum1 - min1)
    else:
        print(sum0 + sum1 - min2 - min3)
elif (sum0 % 2 == 1) and (sum1 % 2 == 1):
    if min2 < min3 + min1:
        print(sum0 + sum1 - min2)
    else:
        print(sum0 + sum1 - min3 - min1)
elif (sum0 % 2 == 0) and (sum1 % 2 == 0):
    if min3 < min2 + min1:
        print(sum0 + sum1 - min3)
    else:
        print(sum0 + sum1 - min2 - min1)


##Тип 27 № 47024

f = open("27-B.txt")
n = int(f.readline())
lefts = [0 for i in range(1111)]
count = 0
sumi = 0
for i in range(1, n + 1):
    num = int(f.readline())
    sumi += num
    if sumi % 1111 == 0:
        count = count + 1
    count += lefts[sumi % 1111]
    lefts[sumi % 1111] += 1
print(count)

##Тип 27 № 28133

f = open("27-B.txt")
a = [int(i.strip()) for i in f]
x = 0
y = 0
max_xy = 0
for i in range (len(a)-1):
    for k in range(i+1,len(a)):
        if(a[i]+a[k])%120==0 and max_xy < a[i]+a[k] and a[i] > a[k]:
            x =a[i]
            y = a[k]
            max_xy=a[i]+a[k]
print(x,y)

##
def f(x, dict):
    for key, keybord in dict.items():
        if key == x:
            return keybord


g = open("27-B.txt")
n = int(g.readline())
numbers = [int(x) for x in g]
i = 0
dict = {}
k = 0
maxk = 0
while i != n:
    for h in range(i + 1, n):
        if ((numbers[h] + numbers[i]) % 120 == 0) and (numbers[h] < numbers[i]) and (
                numbers.index(numbers[h]) > numbers.index(numbers[i])):
            dict[numbers[h] + numbers[i]] = numbers[i], numbers[h]
            k = numbers[h] + numbers[i]
            maxk = max(k, maxk)
    i = i + 1
if maxk == 0:
    print('00')
else:
    print('Максимальная сумма:', maxk, '.Искомые элементы:', f(maxk, dict))

## Тип 27 № 36040

f = open("27-B.txt")
n = int(f.readline())
summ = 0
nekr109 = 10000000000000
for i in range(n):
    a,b,c = f.readline().split()
    a = int(a)
    b = int(b)
    c = int(c)
    summ += max(a, b, c)
    n1 = max(a, b, c) - min(a, b, c)
    sr = a+b+c-max(a, b, c) - min(a, b, c)
    n2 = max(a, b, c) - sr
    if n1%109!=0:
        nekr109 = min(nekr109, n1)
    if n2%109!=0:
        nekr109 = min(nekr109, n2)
if summ%109!=0:
    print(summ)
else:
    print(summ-nekr109)

##Тип 27 № 48475
def divideOnTwo(x):
    count = 0
    while x % 2 == 0:
        count += 1
        x = x // 2
    if count > 12:
        count = 12
    return count

with open('27-B.txt') as file:
    n = int(file.readline())
    l = [int(s) for s in file]
d = [[0] * 13 for i in range(3)]
count = 0
result = 0
for i in range(0, n):
    for j in range(12 - divideOnTwo(l[i]), 12 + 1):
        result += d[(3 - l[i] % 3) % 3][j]
    d[l[i] % 3][divideOnTwo(l[i])] += 1
print(result)

##Тип 27 № 33772

f = open("27-B.txt")
s = f.readlines()
n = int(s[0])
sum = 0
dif1 = 20001
dif2 = 20001
dif3 = 20001
dif4 = 20001
count0 = 0
count1 = 0
for i in range(1, n + 1):
    x, y = map(int, s[i].split())
    if x < y:
        sum = sum + x
        if x % 2 == 0: count0 = count0 + 1
        else: count1 = count1 + 1
        if x % 2 != y % 2:
            if (y - x < dif1) and (y % 2 != 0):
                dif2 = dif1
                dif1 = y - x
            elif (y - x < dif2) and (y % 2 != 0): dif2 = y - x
            if (y - x < dif3) and (y % 2 == 0):
                dif4 = dif3
                dif3 = y - x
            elif (y - x < dif4) and (y % 2 == 0):
                dif4 = y - x
    else:
        if y % 2 == 0: count0 = count0 + 1
        else: count1 = count1 + 1
        sum = sum + y
        if x % 2 != y % 2:
            if (x - y < dif1) and (x % 2 != 0):
                dif2 = dif1
                dif1 = x - y
            elif (x - y < dif2) and (x % 2 != 0):
                dif2 = x - y
            if (x - y < dif3) and (x % 2 == 0):
                dif4 = dif3
                dif3 = x - y
            elif (x - y < dif4) and (x % 2 == 0):
                dif4 = x - y
if count1 > count0:
    if sum % 2 == 1:
        print(sum)
    elif dif1 <= dif3:
        print(sum + dif1)
    elif (count1 - count0) != 1:
        print(sum + dif3)
    elif (dif3 + dif4) < dif1:
        print(sum + dif3 + dif4)
    else: print(sum + dif1)
else:
    if sum % 2 == 0:
        print(sum)
    elif dif3 <= dif1:
        print(sum + dif3)
    elif (count0 - count1) != 1:
        print(sum + dif1)
    elif (dif1 + dif2) < dif3:
        print(sum + dif1 + dif2)
    else: print(sum + dif3)

##Тип 27 № 40743

f = open("27-B.txt")
n = int(f.readline())
lefts = [0 for i in range(30)]
maxsum = 0
for i in range(30):
    lefts[i] = 2 * 1000000000
    count = 0
    sum = 0
for i in range(1, n + 1):
    num = int(f.readline())
    sum = sum + num
    if (num % 2 == 0) and (num > 0):
        count = count + 1
    d = count % 30
    if sum < lefts[d]:
        lefts[d] = sum
    maxsum = max(maxsum, sum - lefts[d])
print(maxsum)

##Тип 27 № 35485


f = open("27-B.txt")
n = int(f.readline())
a = list(map(int, f.readlines()))
a.sort()
b_0 = [i for i in a if i % 3 == 0][-3:]
b_1 = [i for i in a if i % 3 == 1][-3:]
b_2 = [i for i in a if i % 3 == 2][-3:]
print(max(sum(b_0), sum(b_1), sum(b_2), b_1[-1] + b_2[-1] + b_0[-1]))


##Тип 27 № 28131
def f(x,dict):
    for key,keybord in dict.items():
        if key==x:
            return keybord


f = open("27-B.txt")
n=int(g.readline())
numbers=[int(x) for x in f]
i=0
dict={}
k=0
maxk=0
while i!=n:
    for h in range(i+1,n):
        if ((numbers[h]+numbers[i]) % 120 ==0) and (numbers[h] < numbers[i]) and (numbers.index(numbers[h]) > numbers.index(numbers[i])):
            dict[numbers[h]+numbers[i]]=numbers[i],numbers[h]
            k=numbers[h]+numbers[i]
            maxk=max(k,maxk)
    i=i+1
if maxk==0:
    print('00')
else:print('максимальная сумма:',maxk,'.Искомые элементы:',f(maxk,dict))

## Тип 27 № 39256
f = open("27-B.txt")
n = int(f.readline())
lefts = [0 for i in range(10)]
rights = [0 for i in range(10)]
for i in range(10):
    lefts[i] = 0
    rights[i] = 0
count = 0
sum = 0
for i in range(1, n + 1):
    num = int(f.readline())
    sum = sum + num
    if num % 2 == 1:
        count = count + 1
    d = count % 10
    if lefts[d] == 0:
        lefts[d] = sum
    rights[d] = sum
maxsum = 0
if count % 10 == 0:
    print(sum)
else:
    for i in range(count % 10 + 1):
        if (rights[i] - lefts[i]) > maxsum:
            maxsum = rights[i] - lefts[i]
if rights[0] > maxsum:
    maxsum = rights[0]
print(maxsum)

## Тип 27 № 33529
f = open("27-B.txt")
s = f.readlines()
n = int(s[0])
sum = 0
dif1 = 20001
dif2 = 20001
dif3 = 20001
dif4 = 20001
count0 = 0
count1 = 0
for i in range(1, n + 1):
    x, y = map(int, s[i].split())
    if x > y:
        sum = sum + x
        if x % 2 == 0: count0 = count0 + 1
        else: count1 = count1 + 1
        if x % 2 != y % 2:
            if (x - y < dif1) and (x % 2 != 0):
                dif2 = dif1
                dif1 = x - y
            elif (x - y < dif2) and (x % 2 != 0): dif2 = x - y
            if (x - y < dif3) and (x % 2 == 0):
                dif4 = dif3
                dif3 = x - y
            elif (x - y < dif4) and (x % 2 == 0):
                dif4 = x - y
    else:
        if y % 2 == 0: count0 = count0 + 1
        else: count1 = count1 + 1
        sum = sum + y
        if x % 2 != y % 2:
            if (y - x < dif1) and (y % 2 != 0):
                dif2 = dif1
                dif1 = y - x
            elif (y - x < dif2) and (y % 2 != 0):
                dif2 = y - x
            if (y - x < dif3) and (y % 2 == 0):
                dif4 = dif3
                dif3 = y - x
            elif (y - x < dif4) and (y % 2 == 0):
                dif4 = y - x
if count1 > count0:
    if sum % 2 == 1:
        print(sum)
    elif dif3 <= dif1:
        print(sum - dif3)
    elif (count1 - count0) != 1:
        print(sum - dif1)
    elif (dif1 + dif2) < dif3:
        print(sum - dif1 - dif2)
    else: print(sum - dif3)
else:
    if sum % 2 == 0:
        print(sum)
    elif dif1 <= dif3:
        print(sum - dif1)
    elif (count0 - count1) != 1:
        print(sum - dif3)
    elif (dif3 + dif4) < dif1:
        print(sum - dif3 - dif4)
    else: print(sum - dif1)

##Тип 27 № 27991
f = open("27-B.txt")
s = f.readlines()
n = int(s[0])
max_ch = 0
max_n = 0
max_ch17 = 0
max_n17 = 0
for i in range(1, n + 1):
    s[i] = int(s[i])
    if s[i] % 2 == 0:
        if s[i] % 17 == 0 and s[i] > max_ch17:
            max_ch17 = s[i]
        elif s[i] % 17 == 0 and s[i] <= max_ch17:  # поиск второго максимума
            if s[i] > max_ch:
                max_ch = s[i]
        elif s[i] > max_ch:
            max_ch = s[i]
    elif s[i] % 2 != 0:
        if s[i] % 17 == 0 and s[i] > max_n17:
            max_n17 = s[i]
        elif s[i] % 17 == 0 and s[i] <= max_n17:
            if s[i] > max_n:
                max_n = s[i]
        elif s[i] > max_n:
            max_n = s[i]
if max_n17 + max_n == 0 and max_ch17 + max_ch == 0:
    print(0, 0)
elif max_n17 + max_n > max_ch17 + max_ch:
    print(max_n17, max_n)
else:
    print(max_ch17, max_ch)

## Тип 27 № 46985
f = open("27-B.txt")
n = int(f.readline())
lefts = [0 for i in range(1000)]
count = 0
sumi = 0
for i in range(1, n + 1):
    num = int(f.readline())
    sumi += num
    if sumi % 999 == 0:
        count = count + 1
    count += lefts[sumi % 999]
    lefts[sumi % 999] += 1
print(count)

## Тип 27 № 28129
f = open("27-B.txt")
s = int(f.readline()); k7 = 0; res = []
for a in range(s):
    x = int(f.readline())
    if x % 7 == 0:
        k7 = max(k7, x)
    res += [x]
print(k7, max(res))

##Тип 27 № 27424
f = open("27-B.txt")
s = f.readlines()
n = int(s[0])  # количество пар
summi = 0
d = 10**6
for i in range(1, n + 1):
    x, y = map(int, s[i].split())
    summi += max(x, y)
    if abs(x - y) % 3 != 0:
        d = min(d, abs(x - y))
if summi % 3 != 0:
    print(summi)
else:
    print(summi - d)

## Тип 27 № 27891
f = open("27-B.txt")
s = f.readlines()
n = int(s[0])
maxi = 0
max_0 = 0
max_2 = 0
max_7 = 0
max_14 = 0
for i in range(1, n + 1):
    s[i] = int(s[i])
    if s[i] % 14 == 0:
        max_14 = max(max_14, s[i])
    elif s[i] % 7 == 0:
        max_7 = max(max_7, s[i])
    elif max_2 % 2 == 0:
        max_2 = max(max_2, s[i])
    else:
        max_0 = max(max_0, s[i])
maxi = max(max_14 * max(max_7, max_0, max_2), max_7 * max_2)
print(maxi)

##Тип 27 № 27989
f = open("27-B.txt")
s = f.readlines()
n = int(s[0])
k = 0
k_0 = 0
k_26 = 0
k_2 = 0
k_13 = 0
for i in range(1, n + 1):
    s[i] = int(s[i])
    if s[i] % 26 == 0:
        k_26 += 1
    elif s[i] % 13 == 0:
        k_13 += 1
    elif s[i] % 2 == 0:
        k_2 += 1
    else:
        k_0 += 1
k = k_26 * k_0 + k_13 * k_2 + k_26 * k_13 + k_26 * k_2 + (k_26 * (k_26 - 1)) // 2
print(k)

##Тип 27 № 28130
f = open("27-B.txt")
n=int(f.readline())
numbers=[int(x) for x in f]
i=0
k=0
while i!=n:
    for h in range(i+1,n):
        if (numbers[i]+numbers[h])%80==0 and (numbers[i]>50 or numbers[h]>50):
            k=k+1
    i=i+1
print(k)

##Тип 27 № 27990
f = open("27-B.txt")
s = f.readlines()
n = int(s[0])
k = 0
k_0 = 0
k_62 = 0
k_2 = 0
k_31 = 0
for i in range(1, n + 1):
    s[i] = int(s[i])
    if s[i] % 62 == 0:
        k_62 += 1
    elif s[i] % 31 == 0:
        k_31 += 1
    elif s[i] % 2 == 0:
        k_2 += 1
    else:
        k_0 += 1
k = k_62 * k_0 + k_31 * k_2 + k_62 * k_31 + k_62 * k_2 + (k_62 * (k_62 - 1)) // 2
print(k)

##Тип 27 № 27889
f = open("27-B.txt")
n = int(f.readline())
s = 0
minn = 20001
d = 0
for i in range(n):
    x, y = map(int, f.readline().split())
    s += min(x, y)
    d = abs(x-y)
    if d % 3 != 0:
        minn = min(d, minn)
if s % 3 !=0:
    print(s)
else:
    print(s+minn)
f.close()
##Тип 27 № 27890
f = open("27-B.txt")
n = int(f.readline())
s, minn = 0, 20001
for i in range(n):
    x, y = map(int, f.readline().split())
    s += max(x, y)
    d = abs(x - y)
    if d % 5 != 0 :
        minn = min(d, minn)
if s % 5 != 0:
    print(s)
else:
    print(s - minn)

##Тип 27 № 48448
f = open("27-B.txt")
n=int(f.readline())
numbers=[int(x) for x in f]
i=0
k=0
while i!=n:
    for h in range(i+1,n):
        if (numbers[i]+numbers[h])%3==0 and (numbers[i]*numbers[h])%1024==0:
            k=k+1
    i=i+1
print(k)
