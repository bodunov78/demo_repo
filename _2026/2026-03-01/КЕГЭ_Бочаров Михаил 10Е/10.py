with open() as f:
a=f.read
k=1
while '' in a:
    k=k+1
print(k)
