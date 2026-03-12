#1
c=[]
k=0
for i in range (-100000,0):
    if i%15==0:
        c.append (i)
        k=k+1
    if k==100:
        break  
print(c)
#2
k=0
v=0
c=[]
for i in range (-10000,0):
    if k<100:
        v=v-15
        c.append(v)
        k=k+1
print(c)
      
