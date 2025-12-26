##Тип 26 № 41001
f = open('26.txt')
n = int(f.readline())
start_time = 1634515199
end_time = start_time + 604800
count = 0
time_process = [0 for i in range(604801)]
for i in f:
    start_process, end_process = i.split()
    if (int(start_process) < start_time) and ((int(end_process) > start_time) or (int(end_process) == 0)):
        count = count + 1
    if (int(start_process) >= start_time) and (int(start_process) <= end_time):
        time_process[int(start_process) - start_time] = time_process[int(start_process) - start_time] + 1
    if (int(end_process) >= start_time) and (int(end_process) <= end_time):
        time_process[int(end_process) - start_time] = time_process[int(end_process) - start_time] - 1
sum_time = 0
max_process = 0
for i in range(1, 604801):
    count = count + time_process[i]
    if count > max_process:
        max_process = count
        sum_time = 0
    if count == max_process:
        sum_time = sum_time + 1
print(max_process, sum_time)

##Тип 26 № 40742
f = open("26 (7).txt")
n = int(f.readline())
start_time = 1633305600
end_time = start_time + 604800
count = 0
time_process = [0 for i in range(0, 604801)]
for i in f:
    start_process, end_process = i.split()
    if (int(start_process) < start_time) and ((int(end_process) > start_time) or (int(end_process) == 0)):
        count = count + 1
    if (int(start_process) >= start_time) and (int(start_process) <= end_time):
        time_process[int(start_process) - start_time] = time_process[int(start_process) - start_time] + 1
    if (int(end_process) >= start_time) and (int(end_process) <= end_time):
        time_process[int(end_process) - start_time] = time_process[int(end_process) - start_time] - 1
sum_time = 0
max_process = 0
for i in range(1, 604801):
    count = count + time_process[i]
    if count > max_process:
        max_process = count
        sum_time = 0
    if count == max_process:
        sum_time = sum_time + 1
print(max_process, sum_time)

##Тип 26 № 33528
f = open('26.txt')
x, y = f.readline().split()
y = int(y)
for_B_price = []
for_B_kol = []
for i in f:
    if 'A' in i:
        a, b, c = i.split()
        y -= int(a) * int(b)
    else:
        a2, b2, c2 = i.split()
        for_B_price.append(int(a2))
        for_B_kol.append(int(b2))
mini = min(for_B_price)
index_mini = 0
for i in range(len(for_B_price)):
    if mini == for_B_price[i]:
        index_mini = i
kol_B = 0
while y > for_B_price[index_mini]:
    y -= for_B_price[index_mini]
    for_B_kol[index_mini] -= 1
    kol_B += 1
    if for_B_kol[index_mini] == 0:
        for_B_price[index_mini] = 1000000000
        mini = min(for_B_price)
        for i in range(len(for_B_price)):
            if mini == for_B_price[i]:
                index_mini = i
print(kol_B, y)
##Тип 26 № 33198
f = open('26 (13).txt')
a, b = f.readline().split()
d = []
s = 0
count = 0
for i in f:
    if 200 <= int(i) <= 210:
        s += int(i)
        count += 1
    else:
        d.append(int(i))
d.sort()
d2 = []
i = 0
while sum(d2) + d[i] <= int(b) - s:
    count += 1
    d2.append(d[i])
    i += 1
k = len(d) - 1
while i > 0:
    while k >= 0:
        if sum(d2) - d2[i-1] + d[k] <= int(b) - s and d[k] != 0:
            d2[i-1] = d[k]
            d[k] = 0
            i -= 1
            break
        else:
            k -= 1
s += sum(d2)
print(count, s)

## Тип 26 № 36000

f = open('inf_26_04_21_26.txt')
k = f.readlines()
n = list(map(int, k))
m = 0
s = 0
c = 0
ns = set(n)
for i in range(1, len(n) - 1):
    for j in range(i + 1, len(n)):
        if ((n[i] + n[j]) % 2 == 1):
            s = n[i] + n[j]
            if (s in ns):
                c += 1
                if s > m:
                    m = s

print(c, m)
##Тип 26 № 38960
f = open('26.txt')
n, m = f.readline().split()
arrayAB = [[0] * 2 for i in range(916)]
arrayA = [[0] * 2 for i in range(916)]
n = int(n)
m = int(m)
count = 0
sumi = 0
for i in range(n):
    x, z = f.readline().split()
    arrayAB[i][0] = int(x)
    if z == 'A':
        arrayAB[i][1] = 0
    if z == 'B':
        arrayAB[i][1] = 1
arrayAB.sort()
i = 0
while m > arrayAB[i][0] + sumi:
    if (sumi + arrayAB[i][0]) < m:
        sumi = sumi + arrayAB[i][0]
        count += 1
    i += 1
x = 1
for i in range(count, n):
    if arrayAB[i][1] == 0:
        arrayA[x][0] = arrayAB[i][0]
        arrayA[x][1] = arrayAB[i][1]
        x += 1
x = 1
for i in range(count - 1, -1, -1):
    if arrayAB[i][1] == 1:
        if (sumi - arrayAB[i][0] + arrayA[x][0]) > m:
            break
        sumi = sumi - arrayAB[i][0] + arrayA[x][0]
        arrayAB[i][0] = arrayA[x][0]
        arrayAB[i][1] = arrayA[x][1]
        x += 1
countA = 0
for i in range(count):
    if arrayAB[i][1] == 0:
        countA = countA + 1
print(countA, m - sumi)

##Тип 26 № 45260
f = open("107_26.txt")
n = int(f.readline())
nums = list()
for i in f:
    a, b = i.split()
    a = int(a)
    b = int(b)
    nums.append([a, -b])
nums.sort()
r = 0
m = 0
for i in range(1, n - 1):
    if nums[i][0] == nums[i - 1][0]:
        if nums[i][1] - nums[i - 1][1] == 14:
            r = nums[i][0]
            m = -nums[i][1] + 1
print(r, m)

##Тип 26 № 33105
f = open('inf_22_10_20_26 (1).txt')
a = []
n = int(f.readline()) # Удаляем первую строку(общее количество купленных товаров)
s = 0
maxi = 0
for i in f:
    x = int(i)
    if x <= 100:
        s += x
    else:
        a.append(x)
a.sort()
for i in range(len(a)):
    if i < len(a)//2:
        s += a[i] * 0.70
        maxi = a[i]
    else:
        s += a[i]
print(round(s), maxi)

## Тип 26 № 33496
f = open('26.txt')
a, b = f.readline().split()
d = []
s = 0
count = 0
for i in f:
    if 210 <= int(i) <= 220:
        s += int(i)
        count += 1
    else:
        d.append(int(i))
d.sort()
d2 = []
i = 0
while sum(d2) + d[i] <= int(b) - s:
    count += 1
    d2.append(d[i])
    i += 1
k = len(d) - 1
while i > 0:
    while k >= 0:
        if sum(d2) - d2[i-1] + d[k] <= int(b) - s and d[k] != 0:
            d2[i-1] = d[k]
            d[k] = 0
            i -= 1
            break
        else:
            k -= 1
s += sum(d2)
print(count, s)

##Тип 26 № 37161
f = open(26.txt’)

n = int(f.readline())

nums = []

for _ in range(n):

    pair = list(map(int, f.readline().split()))

    pair[1] = -pair[1]

    nums += [pair]

nums.sort()

r, m = 0, 0

for i in range(1, len(nums)):

    if nums[i][0] == nums[i-1][0]:

        if nums[i][1] – nums[i-1][1] == 3:

            r = nums[i][0]

            m = -nums[i][1] + 1

print(r, m)

## Тип 26 № 39255
f = open('26 (11).txt')
n, m = f.readline().split()
arrayAB = [[0] * 2 for i in range(916)]
arrayB = [[0] * 2 for i in range(916)]
n = int(n)
m = int(m)
count = 0
sumi = 0
for i in range(n):
    x, z = f.readline().split()
    arrayAB[i][0] = int(x)
    if z == 'B':
        arrayAB[i][1] = 0
    if z == 'A':
        arrayAB[i][1] = 1
arrayAB.sort()
i = 0
while m > arrayAB[i][0] + sumi:
    if (sumi + arrayAB[i][0]) < m:
        sumi = sumi + arrayAB[i][0]
        count += 1
    i += 1
x = 1
for i in range(count, n):
    if arrayAB[i][1] == 0:
        arrayB[x][0] = arrayAB[i][0]
        arrayB[x][1] = arrayAB[i][1]
        x += 1
x = 1
for i in range(count - 1, -1, -1):
    if arrayAB[i][1] == 1:
        if (sumi - arrayAB[i][0] + arrayB[x][0]) > m:
            break
        sumi = sumi - arrayAB[i][0] + arrayB[x][0]
        arrayAB[i][0] = arrayB[x][0]
        arrayAB[i][1] = arrayB[x][1]
        x += 1
countB = 0
for i in range(count):
    if arrayAB[i][1] == 0:
        countB = countB + 1
print(countB, m - sumi)

##Тип 26 № 47023
f = open('26 (17).txt')
n = int(f.readline())
maxlen = 0
screen = [['0'] * 10001 for i in range(10001)]
for i in f:
    x, y = i.split()
    screen[int(x)][int(y)] = '1'
for i in range(1, 10001):
    count = 0
    for j in range(1, 10001):
        if j % 2 != 0:
            if (screen[i][j] == '1') and (screen[i][j + 1] == '0'):
                count = count + 1
            else:
                if count > maxlen:
                    maxlen = count
                    maxnum = i
                count = 0
print(maxlen, maxnum)

##Тип 26 № 48474
f = open('26.txt')
n = f.readline()
cubes = sorted([int(i) for i in f], reverse=True)
cklad=[]
while len(cubes)>0:
    block = [cubes.pop(0)]
    for i in range(len(cubes)):
        if (block[-1]-cubes[i])>=7:
            block.append(cubes[i])
            cubes[i]=''
    cubes=[x for x in cubes if x!='']
    cklad.append(block)
print(len(cklad),max(len(c) for c in cklad))

## Тип 26 № 35915
with open('26.txt') as f:
    numbers = [int(x) for x in f]
    numbers4 = [int(x) for x in numbers if int(x) % 2 != 0]
    i = 0
    k = 0
    sr = 0
    maxsr = 0
    while i != len(numbers4):
        for h in range(i + 1, len(numbers4)):
            if ((numbers4[i] + numbers4[h]) // 2) in numbers:
                k = k + 1
                sr = ((numbers4[i] + numbers4[h]) // 2)
                maxsr = max(sr, maxsr)
        i = i + 1
print(k, maxsr)
##
f = open('26.txt')
k = f.readlines()
n = list(map(int, k))
m = 0
s = 0
c = 0
ns = set(n)
for i in range(1, len(n) - 1):
    for j in range(i + 1, len(n)):
        if n[i] % 2 != 0 and n[j] % 2 != 0:
            s = (n[i] + n[j]) // 2
            if s in ns:
                c += 1
                if s > m:
                    m = s
print(c, m)

##Тип 26 № 29674
import math
f = open('inf_22_10_20_26.txt')
a = []
m = int(f.readline())  # Удаляем первую строку(общее количество купленных товаров)
s = 0
maxi = 0
for i in f:
    x = int(i)
    if x <= 50:
        s += x
    else:
        a.append(x)
a.sort()
for i in range(len(a)):
    if i < len(a)//2:
        s += a[i] * 0.75
        maxi = round(a[i])
    else:
        s += a[i]
print(math.ceil(s), maxi)

##Тип 26 № 47230
f = open('26.txt')
n = f.readline()
boxes = sorted([int(i) for i in f], reverse=True)
answer = [boxes[0]]
for box in boxes[1:]:
    if answer[-1] - box >= 3:
        answer.append(box)
print(len(answer), answer[-1])

##Тип 26 № 46984

f = open('26 (11).txt')
n = int(f.readline())
a = [[0] * 10001 for j in range(10001)]
for i in range(n):
    x, y = map(int, f.readline().split())
    a[x][y] = 1
maxi = 0
mini = 0
for i in range(10001):
    count = 0
    m = 0
    for j in range(10001):
        if a[i][j] == 1:
            count += 1
            m = max(count, m)
        else:
            count = 0
    if m > maxi:
        maxi = max(maxi, m)
        mini = i
print(maxi, mini)

##Тип 26 № 33771
f = open('26 (4).txt')
x, y = f.readline().split()
y = int(y)
for_A_price = []
for_A_kol = []
for i in f:
    if 'B' in i:
        a, b, c = i.split()
        y -= int(a) * int(b)
    else:
        a2, b2, c2 = i.split()
        for_A_price.append(int(a2))
        for_A_kol.append(int(b2))
mini = min(for_A_price)
index_mini = 0
for i in range(len(for_A_price)):
    if mini == for_A_price[i]:
        index_mini = i
kol_B = 0
while y > for_A_price[index_mini]:
    y -= for_A_price[index_mini]
    for_A_kol[index_mini] -= 1
    kol_B += 1
    if for_A_kol[index_mini] == 0:
        for_A_price[index_mini] = 1000000000
        mini = min(for_A_price)
        for i in range(len(for_A_price)):
            if mini == for_A_price[i]:
                index_mini = i
print(kol_B, y)

##Тип 26 № 36881
f = open('inf_26_04_21_26.txt')
k = f.readlines()
n = list(map(int, k))
m = 0
s = 0
c = 0
ns = set(n)
for i in range(1, len(n) - 1):
    for j in range(i + 1, len(n)):
        if ((n[i] + n[j]) % 2 != 1):
            s = n[i] + n[j]
            if (s in ns):
                c += 1
                if s > m:
                    m = s

print(c, m)
#Тип 26 № 35484

f = open('26 (1).txt')
k = f.readlines()
n = list(map(int, k))
m = 0
s = 0
c = 0
ns = set(n)
for i in range(1, len(n) - 1):
    for j in range(i + 1, len(n)):
        if n[i] % 2 == 0 and n[j] % 2 == 0:
            s = (n[i] + n[j]) // 2
            if s in ns:
                c += 1
                if s > m:
                    m = s
print(c, m)

##Тип 26 № 28132
f = open('28132.txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])  # первая строка больше не нужна, удаляем ее
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
for count in range(0, len(data)):
    if summa + data[count] > s: break
    summa += data[count]
print(count)
zapas = s - summa
for i in range(0, len(data)):
    if data[i] - data[count - 1] <= zapas:
        itog = data[i]
print(itog)

##Тип 26 № 28140
f = open('28140.txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])  # первая строка больше не нужна, удаляем ее
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
for count in range(0, len(data)):
    if summa + data[count] > s: break
    summa += data[count]
print(count)
zapas = s - summa
for i in range(0, len(data)):
    if data[i] - data[count - 1] <= zapas:
        itog = data[i]
print(itog)

##Тип 26 № 27887
f = open('27887.txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])  # первая строка больше не нужна, удаляем ее
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
for count in range(0, len(data)):
    if summa + data[count] > s: break
    summa += data[count]
print(count)
zapas = s - summa
for i in range(0, len(data)):
    if data[i] - data[count - 1] <= zapas:
        itog = data[i]
print(itog)

##Тип 26 № 27888
f = open('27888.txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])  # первая строка больше не нужна, удаляем ее
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
for count in range(0, len(data)):
    if summa + data[count] > s: break
    summa += data[count]
print(count)
zapas = s - summa
for i in range(0, len(data)):
    if data[i] - data[count - 1] <= zapas:
        itog = data[i]
print(itog)

##Тип 26 № 28139
f = open('28139.txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])  # первая строка больше не нужна, удаляем ее
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
for count in range(0, len(data)):
    if summa + data[count] > s: break
    summa += data[count]
print(count)
zapas = s - summa
for i in range(0, len(data)):
    if data[i] - data[count - 1] <= zapas:
        itog = data[i]
print(itog)

##Тип 26 № 27885
f = open('27885.txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])  # первая строка больше не нужна, удаляем ее
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
for count in range(0, len(data)):
    if summa + data[count] > s: break
    summa += data[count]
print(count)
zapas = s - summa
for i in range(0, len(data)):
    if data[i] - data[count - 1] <= zapas:
        itog = data[i]
print(itog)

##Тип 26 № 28138
f = open('28138.txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])  # первая строка больше не нужна, удаляем ее
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
for count in range(0, len(data)):
    if summa + data[count] > s: break
    summa += data[count]
print(count)
zapas = s - summa
for i in range(0, len(data)):
    if data[i] - data[count - 1] <= zapas:
        itog = data[i]
print(itog)

##Тип 26 № 27886
f = open('27886.txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])  # первая строка больше не нужна, удаляем ее
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
for count in range(0, len(data)):
    if summa + data[count] > s: break
    summa += data[count]
print(count)
zapas = s - summa
for i in range(0, len(data)):
    if data[i] - data[count - 1] <= zapas:
        itog = data[i]
print(itog)

## Тип 26 № 27882
f = open('27882.txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])  # первая строка больше не нужна, удаляем ее
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
for count in range(0, len(data)):
    if summa + data[count] > s: break
    summa += data[count]
print(count)
zapas = s - summa
for i in range(0, len(data)):
    if data[i] - data[count - 1] <= zapas:
        itog = data[i]
print(itog)

## Тип 26 № 27884
f = open('27884.txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])  # первая строка больше не нужна, удаляем ее
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
for count in range(0, len(data)):
    if summa + data[count] > s: break
    summa += data[count]
print(count)
zapas = s - summa
for i in range(0, len(data)):
    if data[i] - data[count - 1] <= zapas:
        itog = data[i]
print(itog)

##Тип 26 № 36039
f = open('26 (5).txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])  # первая строка больше не нужна, удаляем ее
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
for count in range(0, len(data)):
    if summa + data[count] > s: break
    summa += data[count]
print(count)
zapas = s - summa
for i in range(0, len(data)):
    if data[i] - data[count - 1] <= zapas:
        itog = data[i]
print(itog)

##Тип 26 № 28141

f = open('28141.txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])  # первая строка больше не нужна, удаляем ее
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
for count in range(0, len(data)):
    if summa + data[count] > s: break
    summa += data[count]
print(count)
zapas = s - summa
for i in range(0, len(data)):
    if data[i] - data[count - 1] <= zapas:
        itog = data[i]
print(itog)

##Тип 26 № 27881
f = open('27881.txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])  # первая строка больше не нужна, удаляем ее
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
for count in range(0, len(data)):
    if summa + data[count] > s: break
    summa += data[count]
print(count)
zapas = s - summa
for i in range(0, len(data)):
    if data[i] - data[count - 1] <= zapas:
        itog = data[i]
print(itog)
##Тип 26 № 27880
f = open('27880.txt')
s, n = map(int, f.readline().split())
v = sorted(map(int, f))
sum, cnt = 0, 0
    for i in range(len(v)):
        if sum + v[i] <= s:
            sum += v[i]
            cnt += 1
biggest_file = v[cnt - 1:][0] + s - sum
while biggest_file not in v:
    biggest_file -= 1
print(cnt, biggest_file)


##Тип 26 № 27423
f = open('26_demo.txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])  # первая строка больше не нужна, удаляем ее
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
for count in range(0, len(data)):
    if summa + data[count] > s: break
    summa += data[count]
print(count)
zapas = s - summa
for i in range(0, len(data)):
    if data[i] - data[count - 1] <= zapas:
        itog = data[i]
print(itog)
##Тип 26 № 27883
f = open('27883.txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])  # первая строка больше не нужна, удаляем ее
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
for count in range(0, len(data)):
    if summa + data[count] > s: break
    summa += data[count]
print(count)
zapas = s - summa
for i in range(0, len(data)):
    if data[i] - data[count - 1] <= zapas:
        itog = data[i]
print(itog)

##Тип 26 № 48447
f = open('26.txt')
n = f.readline()
cubes = sorted([int(i) for i in f], reverse=True)
cklad=[]
while len(cubes)>0:
    block = [cubes.pop(0)]
    for i in range(len(cubes)):
        if (block[-1]-cubes[i])>=5:
            block.append(cubes[i])
            cubes[i]=''
    cubes=[x for x in cubes if x!='']
    cklad.append(block)
print(len(cklad),max(len(c) for c in cklad))

