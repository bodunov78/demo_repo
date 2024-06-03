
#Тип 15 34541
#!!!!!!!!!!!!!!!!!!!!!!

def frange(a,b,c):
    x=a
    m=[]
    while x<b:
        m.append(x)
        x+=c

    return m


P=[x for x in frange(3,38+0.5,0.5)]
Q=[x for x in frange(21,57+0.5,0.5)]

R=[x for x in frange(35,50+0.5,0.5)]

vA=[x for x in frange(0,100+0.5,0.5)]
d=[]


a = []
maxa=-10**19

for nach in range(len(vA)-1):
    for kon in range(nach+1,len(vA)):
        #print (nach,kon)
        A=vA[nach:kon]
        #print (m)
        if all( (((x in Q)<=(x in P))<=(not (x in A))) for x in frange(0,100,0.5)  ):
            if len(A)>maxa:
                print(len(A),A)
                maxa=len(A)
