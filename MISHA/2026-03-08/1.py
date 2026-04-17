
s=[1,0,0,1,0,1,0,1,0,1]
s.append(1)
s.append(0)
g=[8,8,8,9]
# s.extend([9,9])
s.extend(g)
print (s)
s=s[:-2]
print (s)
n=2345
a=[]
while n>0:
    a.append(n%10)
    n=n//10
a=a[::-1]
print (a)