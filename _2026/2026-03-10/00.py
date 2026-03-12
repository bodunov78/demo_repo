from string import *

L=printable[:36]
s="jfr0984p3ojfp034uifr4o3jf34if034ifk34f340f30usdhf8934foef8439fj9438uwqdo3290ei21o3jd0394r04"

a=set(s)-set(L)
print ("aaaa",a)
suma=0
for i in range(1,36,2):
    suma=suma+s.count(L[i])

print (suma,len(s))

n=int(s,36)
print (n)
cnt=0
while n>0:
    ost=n%36
    if ost%2==0:
        cnt+=1
    n=n//36

print (cnt)
