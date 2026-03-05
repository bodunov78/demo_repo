a=[2,24,3,54,32,67]
b=[]
for i in range(len(a)):
    x=a.pop()
    x=x**2
    b.append(x)
b.reverse()
print(sum(b))