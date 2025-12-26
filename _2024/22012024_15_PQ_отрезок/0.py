#Тип 15 8666

def frr(a,b,c):
    x=a
    m=[]
    while x<b:
        m.append(x)
        x+=c

    return m


P=[x for x in frr(25,50+0.5,0.5)]
Q=[x for x in frr(32,47+0.5,0.5)]
A=[x for x in frr(0,1000+0.5,0.5)]
d=[]
for x in frr(0,1000+0.5,0.5):
    if   ( ( (not(x in A)) <=(x in P))<=((x in A)  <=((x in Q)))) :
        d.append(x)




for i in range(len(d)-1):
    if d[i+1]-d[i] >0.5:
        print (d[i+1],d[i])

print(d)


