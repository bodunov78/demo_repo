a=int(input())
b=int(input())
a1=a
b1=b
while a!=0 and b!=0:
    if a>b:
        a=a%b
    else:
        b=b%a
nod=a+b
print('НОД', nod)
print('НОК',a1*b1//nod)
