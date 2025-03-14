from random import *
a=[[randint(1,9) for j in range (3) ] for j in range(3) ]
print (a)



b=[]
for i in range(3):
    b.append([])
    for j in range(3):
        print (a[j][i])
        b[i].append(a[j][i])


print (b)
print (7^10)
print (bin(120)[2:],bin(10)[2:],bin(114)[2:])

s="вапсмпап"
n="хорошо"
for x in s:
    k=ord(x)
    print (k,"1")
    for y in n:
        k=k^ord(y)
        print(y,ord(y),k, "1")
    print (k,"2")

    m="хороош"
    for y in m:
        k=k^ord(y)
        print (k,"3")
    print(chr(k))


print (ord('М'))
print (chr(1052))
