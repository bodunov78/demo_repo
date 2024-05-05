from itertools import *
m=[]
for x in range(1,5+1):
    for y in product("01",repeat=x):
        s="".join(y)
        m.append(s)

print(m)
a=[]


podr=[]
def f(n):
    print (type(n))
    if len(n)>0 and len(max(n)) ==5 :
        a.append(n)
        return 1


    if len(n)>0:
        k = n[-1]
    for i in range(2):

        if len(n)<2:
            n.append(str(i))
        else:
            n.append(str(k)+str(i))


    print(n)
    return f(n)

f(podr)
# print(sum(f(str(i)) for i in range(2)))
print (a)