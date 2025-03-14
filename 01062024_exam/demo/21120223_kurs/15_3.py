# min=30000
# a=[bool(x) for x in range(2,9) if x >3 ]
# print (a)

a = [[] for x in range(4)]

# a=[[]]*4
print (id(a[0]),id(a[1]),id(a[2]),id(a[3]))

a[1].append(5)
print (a)