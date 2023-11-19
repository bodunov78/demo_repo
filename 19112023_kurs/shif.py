from random import *
s="хорошо живет на свете винни-пух, у него жена и дети он лопух"
di_u={}
di_c={}
code=set()

di_u=dict.fromkeys(set(s),'00')
print(len(di_u))

while len(code) !=len(di_u):
    code.add(str(randint(10,99)))

print (code)
i=0
for x in di_u.keys():
    di_u[x]=list(code)[i]
    i+=1

for k,v in di_u.items():
    di_c[v]=k

print(di_c)
l=""
for i in s:
    l+=str(di_u[i])
print (l)
s2=""
for i in range(0,len(l)-1,2):
    s2+=di_c[l[i]+l[i+1]]
print(s2)