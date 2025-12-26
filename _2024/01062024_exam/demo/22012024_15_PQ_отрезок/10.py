#Тип 15 58482

#!!!!!!!!!!!!!!!!!!!!!!

def frange(a,b,c):
    x=a
    m=[]
    while x<b:
        m.append(x)
        x+=c

    return m


P=[x for x in frange(24,77+0.5,0.5)]
Q=[x for x in frange(47,92+0.5,0.5)]

R=[x for x in frange(82,116+0.5,0.5)]

vA=[x for x in frange(0,150+0.5,0.5)]
d=[]


a = []
mina=10**19

for nach in range(len(vA)-1):
    for kon in range(nach+1,len(vA)):
        #print (nach,kon)
        A=vA[nach:kon]
        #print (m)
        if all( (       (not((x in Q) <= (( x in P ) or (x in R))))   <= ( (not(x in A)) <= (not(x in Q)))                                        ) for x in frange(0,100,0.5)  ):
            if len(A)<mina:
                print(len(A),A)
                mina=len(A)
