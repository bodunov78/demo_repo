раурa=input().split()
b=[]
for i in a:
    if  'Z' not in i and 'z' not in i:
        b.append(len(i))
print(max(b))