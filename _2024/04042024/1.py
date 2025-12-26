from random import *
a=[randint(0,100) for x in range(100)]
print (a)
l=a[0]
maxi=-10**19
for i in range(6,len(a)):
        if a[i]+l >maxi:
            maxi=max(maxi,a[i]+max(l,a[i-6]))
            print ((maxi,l,a[i-6],a[i]))
        if a[i-6]>l:
            l=a[i-6]

