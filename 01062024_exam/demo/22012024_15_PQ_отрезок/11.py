#Тип 15 8666

#!!!!!!!!!!!!!!!!!!!!!!

def frange(a,b,c):
    x=a
    m=[]
    while x<b:
        m.append(x)
        x+=c

    return m


P=[x for x in frange(25,50+0.5,0.5)]
Q=[x for x in frange(32,47+0.5,0.5)]
vA=[x for x in frange(0,150+0.5,0.5)]
d=[]



maxa=-10**19

for nach in range(len(vA)-1):
    for kon in range(nach+1,len(vA)):
        #print (nach,kon)
        A=vA[nach:kon]
        #print (m)
        if all( (    ((not(x in A)) <= (x in P)) <= ((x in A) <= (x in Q))                                      ) for x in frange(0,150,0.5)  ):
            if len(A)>maxa:
                print(len(A),A)
                maxa=len(A)
