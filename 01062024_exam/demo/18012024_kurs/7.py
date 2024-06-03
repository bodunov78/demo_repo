from itertools import *
b=[2,1,1,0]
x=[[2,2]]
bn=b[:]
# c=[sum([m*n for m,n in zip(a,b)])]
# print (c)

# c=[[m*n for m,n in zip(a,b)] for b in permutations(bn)]

# c=[sum([m*n for m,n in zip(a,b)]) for b in permutations(bn)]
# print (c)

# c=[sum(map(lambda x,y:x*y,a,b)) for b in permutations(b)]
# print (c)
for a in x:
    k = [a[:i] + a[i + 1:] + [a[i] + 1, a[i] + 1] for i in range(len(a))]
#a = set(tuple(x) for x in k)
    print (k)
def tre(x):
    # x={}
    #x={(2,3,3,3),(2,2,4,4)}
    # print(type(x))
    #x.add((3,))
    nx=set()
    for a in x:
        n=list(a)
        k = tuple()
        for i,v in enumerate(n):
            k=tuple(n[:i])+tuple(n[i+1:]) +(n[i]+1,)+(n[i]+1,)
            nx.add(k)
            k=()

    # print(nx)

    x=nx
    # print(x)
    return x
        # x.remove(a)


        # a.add((j+1,j+1))
        # print(a,j)
x={(1,3)}

for i in range(4):
    x=tre(x)
    print (x)

m=(1,2,3)
mn=tuple([x+1,x+1] if x==1 else x for x in m)


print ("MN",*mn)