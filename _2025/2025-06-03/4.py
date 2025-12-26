a= int(input())
d=[]
for i in range(a):
    b= int(input())
    if b % 10 == 4:
        d.append(b)
if len(d)>0: print(min(d))
