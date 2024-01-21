#Тип 15 14277

def frr(a,b,c):
    x=a
    m=[]
    while x<b:
        m.append(x)
        x+=c

    return m


P=[x for x in frr(17,40+0.5,0.5)]
Q=[x for x in frr(20,57+0.5,0.5)]
A=[x for x in frr(0,100+0.5,0.5)]
d=[]


a = []
mina=10**20

for nach in range(len(A)-1):
    for kon in range(nach+1,len(A)):
        #print (nach,kon)
        m=A[nach:kon]
        # print (m)
        if all( (not(x in m ))<=(((x in P) and (x in Q ))<=(x in m)) for x in frr(0,100,0.5)):
            if len(m)<mina:
                print(len(m),m)
                mina=len(m)
