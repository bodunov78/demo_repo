a=[1,2,3,4,5,4,4,4,4,4,4,4,4]
a.sort(reverse=1)
print (a,type(a))
b=set(a)
print (b,type(b))
b.add(7)
print (b,type(b))
b.remove(5)
print (b,type(b))
print(b.pop())
print (b)
b={1,2,3,4,5,6}
c={4,5,6,7,99,888}
print (c|b)
print (c&b)
print (c-b)
print (b-c)
b=[1,3,5,7,8,9,9]
if len(b)==len(set(b)):
    print (b)
else:
    print ("Uppsss")

