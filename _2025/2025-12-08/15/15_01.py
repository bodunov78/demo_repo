def f(x,a1,a2):
    P=15 <=x<= 142
    Q= 38<=x<= 167
    A=a1<=x<=a2
    return ( not(Q<=(  (  (not(A)) and P          ) <=(not(P))       )                  ))




m=[]
d=[]
for x in (15,38,142,167):
    d.append(x)
    d.append(x+0.01)
    d.append(x-0.01)

for a1 in range(1,200):
    for a2 in range(1,200):
        if any (       (f(x,a1,a2) for x in d )            )==False:
            # print (a2-a1)
            m.append(a2-a1)



print(min(m))