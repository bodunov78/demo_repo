from time import *
def Fn(N):

    No=oct(N)[2:]
    if N%7==0:
        No=No+No[-2:]
    else:
        ost=oct((N%7)*7)[2:]
        No=ost+No
    R=int(No,8)
    return R


a=[]
for i in range(20,100):
    R=Fn(i)
    if R>500:
        a.append((R,i))

print (Fn(57))

print (min(a))
