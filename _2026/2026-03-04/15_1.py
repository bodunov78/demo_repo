# 8666
def f(x,a1,a2):
    P=  25 <= x  <=50
    Q = 32<= x <=47
    A = a1 <= x <=a2
    return (((not(A)) <=P)<=( A <=Q))

d=[]
o=[]

   1   5   8

for x in 25,50,32,47:
    d.append(x)
    d.append(x-0.01)
    d.append(x+0.01)
for a1 in d:
    for a2 in d:
        if all([f(x,a1,a2) for x in range(1,100)]):
            print (a2-a1)
            o.append(a2-a1)
print (max(o))

