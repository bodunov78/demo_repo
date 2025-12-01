from itertools import *
from time import *
from fnmatch import *
from re import *
def mn():
    k = {0, 5, 6, 7, 8, 9}
    m = {5, 6, 1}
    if k | m == k:
        print(k | m)
    print(m - k)
    if len(m - k) == 0:
        print("k-m", len(m - k))
        print(f"k--{k}\nm--{m}")
    else:
        print(f"Fuk m--{m}")


def z1202_0():
    a = [56789, 85758, 77770, 50786]

    for x in a:
        s = str(x)
        if s[0] in "568" and s[0] != s[-1]:
            if s[2] in "579" and s[2] != s[0]:
                if x % 2 == 0:
                    j=1
                    # print(s)

def z1202_1():
    a = [56789, 85758, 77770, 50786]
    m=set(str('056789'))
    for x in range(10_000,99_999+1,2):
        s=str(x)
        ms = set(s)
        if m|ms==m:
            if s[0] in "568" and s[0] != s[-1]:
                if s[2] in "579" and s[2] != s[0]:
                    if x in a:
                        j=1
                        # print(s)

def z1202_2():
    a = [56789, 85758, 77770, 50786]
    m = set('056789')

    a1 = ('5', '6', '8')
    a2 = ('0', '5', '6', '7', '8', '9')
    a3 = ('5', '7', '9')
    a4 = a2
    a5 = ('0', '6', '8')

    for x in product(a1, a2, a3, a4, a5):
        s = "".join(x)
        ms = set(s)
        if m | ms == m:
            if s[0] in "568" and s[0] != s[-1]:
                if s[2] in "579" and s[2] != s[0]:
                    if int(s) in a:
                        j=1

                        # print(s)


def z1202_3():
    a = [56789, 85758, 77770, 50786]
    a1 = ('5', '6', '8')
    a2 = ('0', '5', '6', '7', '8', '9')
    a3 = ('5', '7', '9')
    a4 = a2
    a5 = ('0', '6', '8')
    ans = [int(f'{c1}{c2}{c3}{c4}{c5}') for c1 in a1 for c2 in a2 for c3 in a3 for c4 in a4 for c5 in a5 if c1!=c5 and c1!=c3]
    for x in ans:
        if x in a:
            j=1
            # print(x)



def z1202_4():
    a = [56789, 85758, 77770, 50786]
    a1 = '568'
    a2 = '056789'
    a3 = '579'
    a4 = a2
    a5 = '068'
    ans = [int(f'{c1}{c2}{c3}{c4}{c5}') for c1 in a1 for c2 in a2 for c3 in a3 for c4 in a4 for c5 in a5 if c1!=c5 and c1!=c3]
    for x in ans:
        if x in a:
            j=1
            # print(x)

def z1202_5():
    a = [56789, 85758, 77770, 50786]
    a1 = '568'
    a2 = '056789'
    a3 = '579'
    a4 = a2
    a5 = '068'
    ans = [int(f'{c1}{c2}{c3}{c4}{c5}') for c1 in a1 for c2 in a2 for c3 in a3 for c4 in a4 for c5 in a5 if c1!=c5 and c1!=c3]
    for x in a:
        if x in ans:
            j=1
            # print(x)


def z1202_6():
    a = [56789, 85758, 77770, 50786]
    a1 = '568'
    a2 = '056789'
    a3 = '579'
    a4 = a2
    a5 = '068'
    # ans = [int(f'{c1}{c2}{c3}{c4}{c5}') for c1 in a1 for c2 in a2 for c3 in a3 for c4 in a4 for c5 in a5 if c1!=c5 and c1!=c3]
    for x in a:
        s=str(x)
        if fnmatch(s,'[568][056789][579][056789][068]'):
            if s[0]!=s[-1] and s[0]!=s[2]:
                j=1
                # print(x)


def z1202_7():
    a = [56789, 85758, 77770, 50786]
    a1 = '568'
    a2 = '056789'
    a3 = '579'
    a4 = a2
    a5 = '068'
    # ans = [int(f'{c1}{c2}{c3}{c4}{c5}') for c1 in a1 for c2 in a2 for c3 in a3 for c4 in a4 for c5 in a5 if c1!=c5 and c1!=c3]
    for x in a:
        s=str(x)
        # if findall(r'^[568][056789][579][056789][068]$', s):
        if findall(r'^[568][056789][579][056789][068]$', s):

            print(s)
            # if s[0]!=s[-1] and s[0]!=s[2]:
            #     j=1
            #     # print(x)



# z1202()
z1202_7()
st=time()
k=[]
for i in range(100):
    st = time()
    z1202_6()
    k.append(time()-st)

print (sum(k)/len(k),max(k))