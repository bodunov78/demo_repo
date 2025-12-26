x=int(input())
suma=0
n=0
while x!=0:
    if x%8==0:
        suma+=x
        n+=1
    x=int(input())

if n!=0:
    print (f"{(suma/n):.1f}")
else:
    print ("No")


