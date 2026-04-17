a=set()

a.add(10)
for i in range(5):
    a.add(i)
print (a)
a.add(2)
print (a)
m=[1,2,3,4,3,4,3,4,5,6]
print (set(m))
l="23:456:789:23"
k=l.split(':')
print (set(l.split(':')))