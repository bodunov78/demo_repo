#
#
#P=[x for x in range(130,172)]
#Q=[x for x in range(150,186)]
#A=[x for x in range(100,200)]
#m=0
#for a in range(0,200):
#    k=1
#    for x in range(0, 200):
#        if ( (x in P) <=(  ( (x in Q) and (not (x in A)) )  <=   (not (x in P))   ) ):
#            print ("OK",x,A)
#        else:
#            print("Fuck",x,A)
#            k=0
#            if m==0:
#                m=1
#                A.append(max(A)+1)
#
#            break
#    if k==1 and m==0:
#        A.pop(-1)
#    elif k==1 and m==1:
#        A.pop(0)
#
#print (A)


