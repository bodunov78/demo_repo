a=[2,3,4,5]
b=a[:]
b.append(99)
print (a)
print (b)



# c=[1]*4
# c[1]=8
c=[[] for i in range(4)]
c[1].append(8)
print (c)