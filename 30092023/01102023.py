# from itertools import *
# s = "ABCDEF"

# a = [x for x in product(s, repeat=7) if all(x.count(y) <= 3 for y in set(x))]
# a = [x for x in product(s, repeat=7)]
# b=list(map(a,"".join())

# m = [x for x in a if (all(x.count(y * x.count(y)) == 1 for y in set(x)))]
# m=list(map(lambda x: "".join(x),a))


a=[8,2,3,4,5,6]
# b=a
b=a[:]
a[1]=10
# del(a[0])
print(sorted(a),a,b)
a.sort(reverse=1)
print(a)

# различие переменных и списков
#
# c=1
# d=c
# # c=4
# print (c,d,id(c),id(d))
#
# m=[1,2,3]
# n=m
# n[1]=8
# print (m,n,id(m),id(n))

x=a.pop(1)
print (a,x)
# a.reverse()
a=a[::-1]
print(a)

for i,x in enumerate(a):
    if 10<=x<=99:
        print (i,x)
        a[i]="!"

print(a)
m=list(set(a))
print (type(a),type(m),a,m)