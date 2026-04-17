34543
def f(x,a1,a2):
    P=  3 <= x  <=13
    Q = 12<= x <=22
    A = a1 <= x <=a2
    return ((A) <=( (P or Q) ))

d=[]
o=[]
for x in 3,13,12,22:
    d.append(x)
    d.append(x-0.01)
    d.append(x+0.01)
for a1 in d:
    for a2 in d:
        if all([f(x,a1,a2) for x in range(1,100)]):
            print (a2-a1)
            o.append(a2-a1)
print (max(o))

