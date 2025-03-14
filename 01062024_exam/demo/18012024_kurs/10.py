from fnmatch import *
a=[bin(x)[2:].zfill(y) for x in range(20) for y in range(1,5)]
# print (a)

b=['010','011','10']
a=[bin(x)[2:].zfill(y) for x in range(16) for y in range(1,5)]
a=list(set(a))
print (a)
for k in a:
    for m in b:
        if fnmatch(k,f"{m}*"):
            a.remove(k)



a=[]
for x in range(10):
    for y in range(10,20):
        a.append((x,y))

# print (a)