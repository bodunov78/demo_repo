a={1,2,3,4,5,6,7,7}
b={5,6,7,8,9,10}

print (set(a|b)) # U
print (set(a&b)) # n
print (set(a-b)) #A- A&B
print (set(b-a)) #B-A&B
print(set(a^b))   # AuB - AnB

print (a,b)


a.add(100)
print(a)
a.discard(1)
print(a)
print (a&b)


c=set(range(1,100))
d=set(range(-1*10**6,20+1))
print (len(d))
print (c&d)