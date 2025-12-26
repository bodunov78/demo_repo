
#Тип 15 34541
#!!!!!!!!!!!!!!!!!!!!!!


P=[x for x in range(3,38+1)]
Q=[x for x in range(21,57+1)]

R=[x for x in range(35,50+1)]

vA=[x for x in range(0,100+1)]
d=[]


a = []
maxa=-10**19

for nach in range(len(vA)-1):
    for kon in range(nach+1,len(vA)):
        #print (nach,kon)
        A=vA[nach:kon]
        #print (m)
        if all( (((x in Q)<=(x in P))<=(not (x in A))) for x in range(0,100+1)  ):
            if len(A)>maxa:
                print(A)
                maxa=len(A)
