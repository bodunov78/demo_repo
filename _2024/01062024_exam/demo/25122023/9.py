a=set(range(2,99+1))
print (a)
c=set()
a={21,22,23,24}
b={i for i in range(10)}
# c=a
# for x in b:
#     c.add(x)
# print (c)
# print (a|b)


a=[2,3,4,5,6,7]
# b=a.copy()
b=a[:]
b[1]=9
print (a,id(a),b,id(b))
c=[[] for i in range(10)]
print(c)
print (id(c[0]),id(c[1]),id(c[2]),id(c[3]))
c[2].append(8)
print (c)


