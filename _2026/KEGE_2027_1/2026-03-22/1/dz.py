# from itertools import product, repeat
from itertools import *

def f1_1():
    a=[]
    for i in range(10_000,66_666+1):
        s=str(i)
        if '7' in s or '8' in s or '9' in s:
            continue
        else:
            a.append(i)

    print (a)

def f1_2():
    a=[]
    for a1 in "123456":
        for a2 in "0123456":
            for a3 in "0123456":
                for a4 in "0123456":
                    for a5 in "0123456":
                        s=a1+a2+a3+a4+a5
                        a.append(int(s))
    print (len(a))

def f1_3():
    def d2k(n,k):
        s=""
        while n>0:
            ost=str(n%k)
            s=ost+s
            n=n//k
        return s
    a=[]
    for i in range(7**4,7**5):
        a.append(int(d2k(i,7)))
    print (len(a))

def f1_4():


    a=[]
    for s in product("0123456",repeat=5):
        # print (s)
        # ss="".join(s)
        if s[0]!='0':
            ss = "".join(s)
            print (s,ss)
            a.append(int(ss))
    print (len(a))


def f1_5():
    a = []
    s1="123456"
    s0="0123456"
    for s in product(s1,s0,s0,s0,s0 ):
        ss = "".join(s)
        a.append(int(ss))
    print(len(a))

def f2_1():
    s=[1,2,3,2,5]
    for i1 in s:
        s1=s[::]
        s1.remove(i1)
        for i2 in s1:
            s2=s1[:]
            s2.remove(i2)
            for i3 in s2:
                s3=s2[:]
                s3.remove(i3)
                for i4 in s3:
                    s4=s3[:]
                    s4.remove(i4)
                    for i5 in s4:
                        print (i1,i2,i3,i4,i5)


def f2_2():
    a=set()
    m=[]
    for i1 in range(5):
        for i2 in range(5):
            for i3 in range(5):
                for i4 in range(5):
                    for i5 in range(5):
                        a={i1,i2,i3,i4,i5}

                        if len(a)==5:
                            m0=[i1, i2, i3, i4, i5]
                            m.append(m0)
                            # m.append(int("".join(a)))
    print (m)

def f3_1():
    a=[1,1,2,3,3,3,2,2,3,4,000]
    for x in a:

            while a.count(x)>1:
                a.remove(x)

    print (a)
def f3_2():
    a=[1,1,2,3,3,3,2,2,3,4,000]
    a=list(set(a))
    print (a)

def f4_1(a):
    # a=[55,33,2,2,1,23,24,3,566,0]
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    # print (a)
    return (a)
def f5_1():
    for l in range(1,5+1):
        for s in product([0,1,2],repeat=l):
            print (s)

# print (f4_1([1,2,2,3,1,2,4,3]))

f1_4()