#1
a=127
c=[]
while a!=0:
 if a%2==0:
    c.append(0)
 else:
    c.append(1)
 a=a//2
c.reverse()
print(c)
#2
print(bin(127))
