
a=[1,2,3,4,6]
b=[2,3,4,5,6]
# a=10
# b=20
# c=a.copy()
c=a[::]
# c=c+77
c.append(777)
print (id(a),id(b),id(c),a,c)
