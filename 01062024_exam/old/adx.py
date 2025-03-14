import sys
#from math import *
#from itertools import *
#from fnmatch import *
#from csv import reader
def min_arr(a,mn,mx):
    if mx==0:
        a1=min(a,key=lambda x: x[mn-1])[mn-1]
        a2 = [r for r in a if r[mn-1] == a1]
        a3 = min(a2,key=lambda x: x[(0-mn)%mn])
        print(a1, a2, a3)
    else:
        a1 = min(a, key=lambda x: x[mn - 1])[mn - 1]
        a2 = [[r[0], r[1]] for r in a if r[mn-1] == a1]
        a3 = max(a2,key=lambda x: x[mx-1])
        print(a1, a2, a3)

def max_arr(a,mx,mn):
    if mn==0:
        a1=max(a,key=lambda x: x[mx-1])[mx-1]
        a2 = [r for r in a if r[mx - 1] == a1]
        a3 = max(a2,key=lambda x: x[(0-mx)%mx])
        print(a1, a2, a3)
    else:
        a1 = max(a, key=lambda x: x[mx - 1])[mx - 1]
        a2 = [r for r in a if r[mx-1] == a1]
        a3 = min(a2,key=lambda x: x[mn-1])
        print(a1, a2, a3)


def sumarr(a,b,r):
    if r==0:
        a.sort(reverse=1)
        b.sort(reverse=1)

        result = [sum(i) for i in zip(a, b)]
    elif r==-1:
        result = [sum(i) for i in zip(a, b)]
    else:
        a.sort(reverse=1)
        b.sort()
        result = [sum(i) for i in zip(a, b)]

    result.sort(reverse=1)
    return result




def add(num):
     # сохраняет копию файла номер.sav
     #print (sys.argv[0])
#    fname="C:\\1\\"+str(num)+".sav"
    fname=str(num)+".sav"
    name=str(num)+".py"
    f = open(name, "r")
    fcp = f.readlines()
    # print(fcp)
    # print(fcp2)
    asa=['\n############_____############\n']
    fc=asa+fcp+asa


    f3=open(fname,"a+")
    for x in range(len(fc)):
        f3.write(fc[x])
    f.close()
    f3.close()
    
def ads():


    f = open("C:\\1\\1.py", "r")
    f2 = open("10.py", "r")
    fcp = f.readlines()
    fcp2 = f2.readlines()
    # print(fcp)
    # print(fcp2)
    asa=['\n############57\n']
    fc3=fcp2+asa
    for i in range(30):
        fc3.append('\n')

    fc=fc3+fcp
    #print(fc)
    f3=open("10.py","w")
    for x in range(len(fc)):
        f3.write(fc[x])
    return sys.argv[0]


def adsn(num):


    f = open("C:\\1\\"+str(num)+".py", "r")
    f2 = open(str(num)+".py", "r")
    fcp = f.readlines()
    fcp2 = f2.readlines()
    # print(fcp)
    # print(fcp2)

     	
    asa=['\n############\n']
    
    fc3=fcp2+asa
    for i in range(30):
        fc3.append('\n')

    fc=fc3+fcp
#    print(fc)
    f3=open(str(num)+".py","w")
    for x in range(len(fc)):
        f3.write(fc[x])
    return sys.argv[0]



def adn(num):
    fname=str(num)+".py"
	
    f2 = open(fname, "r")
    fcp2 = f2.readlines()
    nfcp = []
    end = len(fcp2) - 1
    for i in range(len(fcp2)):
        nfcp.append(fcp2[i])
        if "##########" in fcp2[i]:
            end = i
            break

    f3 = open(fname, "w")
    for x in range(end + 1):
        f3.write(fcp2[x])
        # print (fc[x])


def ade():
     print(3/0)





def adsp(num):


    f = open("C:\\1\\"+str(num)+".py", "r")
    fcp = f.readlines()
    for x in fcp:
         print(x.replace("#",""))
#         print(x)

    print(3/0)   


def new_ard(n):
    a = []
    n=6
    for i in range(1, n + 1):
        # все префиксы, как двоичные числа
        for x in range(2 ** i):
            pfx = bin(x)[2:].zfill(i)
            a.append(pfx)

    print(a)
    return a


def ard(a, r):
    # r=':001'
    a = [x for x in a if not (r in x)]
    for i in range(len(r), 1, -1):
        # print (r[:i])
        a = [x for x in a if x != r[:i]]
    print(len(a), a)
    return a


def ardn(a, r):
    a = [x for x in a if not (x.startswith(r) or r.startswith(x))]
    print("ardn", a)
    return a


def ardm(a):
    a = list(a)

    flag = 1
    for i in range(len(a)):
        for j in range(len(a)):
            if (i != j):
                if a[i].startswith(a[j]) or a[j].startswith(a[i]):
                    # print(i, j)
                    flag = 0
    if flag == 1:
        return a
    else:
        return 0

def fan(q=0,s=0,bgk=0):
    if q==0 and s==0 and bgk==0:
        print("fan(q,s,bgk)")
        print ("[3,1,0],['00','011'],2+3")
    k = new_ard(len(q))
    for x in s:
        k = ardn(k, x)

    print(k[:3])
    summ = 10 ** 20
    print(math.factorial(len(k)) / math.factorial(len(k) - len(q)))
    if input("continue?:") == 'y':
        l4 = list(combinations(k, len(q)))
        l5 = [a for a in l4 if ardm(a)]
        for z in l5:
            y = [len(c) for c in z]
            suma = 0
            if sum(y) < 17:
                for i in range(len(q)): suma = suma + y[i] * q[i]
                summ = min(summ, suma + bgk)
                print(sum(y), y, z, suma + bgk)



