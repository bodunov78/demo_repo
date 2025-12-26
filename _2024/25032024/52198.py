from time import *
ts=time()
a=[]
for i in range(2,59049):
    if 59049 %i ==0:
        a.append(i)
print(a)


for i in range(11):
    print (i,3**i)

a=[[] for i in range(4)]

with open("52198B.txt") as f:
    n=int(f.readline())
    for x in f:
        x=int(x)
        if x%3==0:
            a[x%4].append(x)

    for i in range(4):
        a[i].sort(reverse=1)
    flag=0
    cnt=0
    for i in range(len(a[0])-1):

        for j in range(i+1,len(a[0])):
            if a[0][i]*a[0][j]%59049==0:
                # print(a[0][i]*a[0][j])
               cnt+=1

    print(time()-ts)
    flag=0
    for i in range(len(a[1])):

        for j in range(len(a[3])):
            if a[1][i]*a[3][j]%59049==0:
                # print(a[0][i]*a[1][j])
                cnt+1


    print(time()-ts)
    print(cnt)