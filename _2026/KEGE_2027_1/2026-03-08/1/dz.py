def fufu(a,b,c):
    mina=min(a,b,c)
    maxa=max(a,b,c)
    mida=a+b+c-mina-maxa
#





def f3n(a,b,c):
    a,b,c=    abs(a), abs(b), abs(c)
    print (a,b,c)
    return (min(a,b,c),max(a,b,c),a+b+c -min(a,b,c)-max(a,b,c))

print (f3n(3,-2,-1))

def maxn(x):
    a=x**3
    b=1/x
    c=abs(x)
    return max(a,b,c)

def arrl(a,b,c):
    arr=[]
    a, b, c = min(a, b, c), max(a, b, c), a + b + c - min(a, b, c) - max(a, b, c)
    print (a,b,c)
    while a < b:
        arr.append(a)
        a+=c

    return arr

def arrf(a,b,c):
    arr=[]
    # a, b, c = min(a, b, c), max(a, b, c), a + b + c - min(a, b, c) - max(a, b, c)
    # print (a,b,c)
    while a < b:
        arr.append(a)
        a+=c

    return arr



def arrn(a,b,c):
    arr=[]
    a,b,c=min(a,b,c),max(a,b,c),a+b+c-min(a,b,c)-max(a,b,c)
    while a < b:
        arr.append(a)
        a+=c
        if isinstance(c, float):
            rnd=len(str(c).split('.')[1])
            a = round(a, rnd)

    return arr

# print (arrf(1,10,0.5))


# print (maxn())

# print(fufu(3,1,2))



n=0
s=0.002
rl=len(str(s).split('.')[1])
print (rl)

#
n=0
while n<5:
    s=0.0003
    rl=len(str(s).split('.')[1])

    n+=s
#
    n=round(n,rl)
    print (n,rl)