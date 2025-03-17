from itertools import *
def fu(s,e,c):
    # print (e)
    if len(s)==0:
        # print(e)
        return e
    else:
        # print(e)
        s1=s[::]
        m=[]
        for x in s :

            s1 = s[::]
            e1=e[::]
            e1.append(x)
            c+=1
            s1.remove(x)
            # print(s1,e1)
            # print (e1,s1,c)
            m.append((s1,e1,c))

        # print(m)
        return [fu(*x) for x in m ]


s=list('12345')
e=[]
c=0
# print (s)
m=fu(s,e,c)

a=[]

for group in m:
    a += group

print (a)



