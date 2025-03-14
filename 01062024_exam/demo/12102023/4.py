# a=1
# b=8
# c=2
# d=16
# n=f=a*d+c*b
# m=s=b*d
# while f !=s:
#     if f>s:
#         f-=s
#     else:
#         s-=f
#
# print(n//f,m//f)

from fnmatch import *
N = 0
for a in range(9):
    for b in range(9):
        if a == 5 and b % 2 == 1:
            continue
        for c in range(9):
            if b == 5 and c % 2 == 1 and a % 2 == 1:
                continue
            for d in range(9):
                if c == 5 and b % 2 == 1 and d % 2 == 1:
                    continue
                for e in range(9):
                    if d == 5 and c % 2 == 1 and e % 2 == 1:
                        continue
                    if e == 5 and d % 2 == 1:
                        continue
                    W = str(a) + str(b) + str(c) + str(d) + str(e)
                    if W.count("5") > 1:
                        continue
                    print(W)

                    N += 1
print(N)

a = "012345678"
count = 0
for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            for l in range(len(a)):
                for m in range(len(a)):
                    c = a[i] + a[j] + a[k] + a[l] + a[m]
                    if c.count("5") == 1 and c[0]!="0":
                        b = c.index('5')
                        if b != 0 and b != 4:
                            if c[1] not in '137':
                                count+=1
                            elif b == 4:
                                if c[3] not in '137':
                                    count += 1
print(count)