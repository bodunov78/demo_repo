# 13364 min
def f(x,a1,a2):
    P=  130 <= x  <=171
    Q = 150<= x <=185
    A = a1 <= x <=a2
    return (P <=(Q and (not(A)) )) <= (not(P))

d=[]
o=[]
for x in 130,171,150,185:
    d.append(x)
    d.append(x-0.01)
    d.append(x+0.01)
for a1 in d:
    for a2 in d:
        if all([f(x,a1,a2) for x in range(-500,500)]):
            print (a2-a1)
            o.append(a2-a1)

print (min(o))

