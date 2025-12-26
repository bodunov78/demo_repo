
print('x  y  w  z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F= ((w == x) and (y <= z))
                F1= ((w <= x) <=(y == z))
                if F == 0 and F1 == 1:
                    print(x, y , w , z)

x=''
for i in range(128,256):
    c= bin(i)
    for v in (c):
        if v == 1:
            x= x + '0'
        else:
            x= x+'1'
if i - int(x,2) == 185:
    print(i)

c = 'ВЛТУ'
x=0
for i in (c):
    for i1 in (c):
        for i2 in (c):
            for i3 in (c):
                m= i + i1+ i2+i3
                x+=1
                if x == 98:
                    print(m)

c=114
n=96
print(bin(c))
print(bin(n))
print(2**7+96)

from sys import *
# setrecursionlimit(l000000)
def f(n):
    if n < 15:
        return n
    elif n >=15:
        return f(n % 15)*f(n // 15)
print(f(7560))


x = 49**6 + 7**18 - 21
s = ''
while x != 0:
    s += str(x % 7)
    x //= 7
s = s[::-1]
print(s.count("6"))



for n in range(0,256):
    r = bin(n)[2:]
    r = 11111111 - int(r)
    r = int(str(r),2)
    r = r - n
    if r == 185:
        print(n)



def tt(x):
    return ((x & 25 != 0) <=((x & 9 == 0) <= (x&a != 0)))

for a in range(1, 10000):
    if all(tt(x) == 1 for x in range(1, 10000)):
        print(a)
        break


def f(x, y): 
    if x > y or x == 15:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 2, y)
print(f(3,9) * f(9,20))


# f= open('act.24.txt')
# st = f.readline()
# k =0
# m= 10**19
# y =[]
# for i in range(len(st)-1):
#     if st[i] == 'Т':
#         y.append(i)
# for n in range(len(y)-209):
#     y[n+209] - y[n] +1
#     if k < m:
#         m = k
# print(m)



































