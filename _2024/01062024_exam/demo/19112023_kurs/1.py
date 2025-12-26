from random import *
x=randint(100,999)
print (randint(100,999))
c=set()
while len(c)!=10:
    c.add(randint(10,99))
print (c)




sl="AAA:001:002:003:004:005:006:007:008:009:010:011:012:C13:014:B15"
di={}
dir={}
arr=list(sl.split(':'))
print (arr)

di['A']="AAA"
di['B']="ABB"

stt="сова, открывай, медведь пришел!!!"
stm=set(stt)
print (stm)

di=dict.fromkeys(stm,'AAA')
print (di)

i=1
for x in stm:
    di[x]=str(100+i)
    i+=1
print(di)

for k,v in di.items():
    dir[v]=k

print (dir)


encs=""
for x in stt:
    encs+=di[x]

print (encs)

for i in range(0,len(encs),3):
    # print (encs[i],encs[i+1],encs[i+2])
    print(dir[encs[i:i+3]])



