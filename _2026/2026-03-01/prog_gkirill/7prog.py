a=[22,2424,21,534,32,670]
b=[]
for i in range(len(a)):
    x=a.pop()
    sumax=sum(map(int, str(x)))
    x=x%sumax
    b.append(x)
b.reverse()
print(b)