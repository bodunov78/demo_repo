f=open("17.txt")
n=int(f.readline())
a=[int(x) for x in f]
maxi=0
for i in range(n):
    if (len(a[i])==2):
        maxi=max(maxi,a[i])



for i in range(n-1):
    if   ( len(str(a[i]))==2 and len(str(a[i+1]))!=2 )or (len(str(a[i]))==2 and len(str(a[i+1])) )!=2:
        print (a[i],a[i+1])



print(n,len(a))




