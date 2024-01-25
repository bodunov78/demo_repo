
#Тип 15 34534
def frr(a,b,c):
    x=a
    m=[]
    while x<b:
        m.append(x)
        x+=c

    return m


P=[x for x in frr(2,10+0.5,0.5)]
Q=[x for x in frr(6,14+0.5,0.5)]
A=[x for x in frr(0,100+0.5,0.5)]
d=[]


a = []
maxi=-10**19

for nach in range(len(A)-1):
    for kon in range(nach+1,len(A)):
        #print (nach,kon)
        m=A[nach:kon]
        # print (m)
        if all( (((x in m )<=(x in P)) or (x in Q ))  for x in frr(0,100,0.5)):
            if len(m)>maxi:
                print(len(m),m)
                maxi=len(m)
