from time import  *
def de(x):
    a=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            a.add(i)
            a.add(x//i)
    a=list(a)
    a.sort()
    return a



# print (len(de(12)))

ts=time()
for i in range(123456789,223456789+1):
    if int(i**0.5)**2 == i:
        a=de(i)
        if len(a)==5:
            print (i,a[-2])

print (time()-ts)

