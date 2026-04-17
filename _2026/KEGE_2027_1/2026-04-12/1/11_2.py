f=open("13.txt","r",encoding="utf-8")
# m=f.readlines()
# print (m)
m=[]
for x in f:
    x=x.strip()
    x=int(x)
    m.append(x)
print (m)
f.close()

# for x in m:
#     print (x)
N=10**20
for x in m:
    if x%15!=0:
        N=min(N,x)

for i in range(1,len(m)):
    # print (i,m[i],m[i+1])
    if m[i]%N==0 and m[i-1]%N==0:
        print (m[i],m[i-1])
print ("N",N)

for a1,a2,a3 in zip(m,m[1:],m[2:]):
    print (a1,a2,a3)

#
# for i,v in enumerate(m):
#     print (i,v)