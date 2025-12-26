from time import *
ts=time()
x=100000000
def a3(x):
    m=set()
    for i in range(2,int(x**0.5)):
        if x%i==0:
            m.add(i)
            m.add(x//i)
    print (m,"\n",time()-ts)


def a2(x):
    m=set()
    for i in range(2,x//2+1):
        if x%i==0:
            m.add(i)
            m.add(x//i)
    print(m, "\n", time() - ts)

def a1(x):
    m=set()
    for i in range(2,x):
        if x%i==0:
            m.add(i)

    print(m, "\n", time() - ts)


def a0(x):
    m = set()
    x0=x
    while x>1:
        for i in range(2,x+1):
            if x%i==0:
                m.add(i)
                m.add(x//i)
                m.add(x0//(x//i))
                x=x//i
                print(x,i,m)
                break
    print(m, "\n", time() - ts)


a1(x)

