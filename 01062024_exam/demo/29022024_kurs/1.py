m=[1,2,3,4,4,3]
a=[]
b=list(set(m))
for x in b:
    a.append(m.count(x))
# if a.count(2)==2

print (b,a)

