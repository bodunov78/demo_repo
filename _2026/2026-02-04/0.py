n=1024*9*11*5**5
i=2
a=[]
while n >1:
    while n%i ==0:
        a.append(i)
        n=n//i
    i+=1
print (a)

