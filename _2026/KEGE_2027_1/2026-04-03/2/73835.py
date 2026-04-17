m=[]
with open("73835.txt") as f:
    for s in f:
        a=list(map(int,s.split()))
        m.append(a)
n=list(zip(*m))
print (n[0])

for a in m:
    cnt=0
    for i,x in enumerate(a):
        c=0
        if a.count(x)==1 and n[i].count(x)  >= 330 and x>(sum(a)/len(a)):
            c+=1
    if c==1:
        cnt+=1
print (cnt)

a=[[1,2,3,4,5],[2,3,4,5,6],[6,7,8,9,0]]
b=[[1,2,6],[2,3,7],[3,4,8],[4,5,9],[5,6,0]]

