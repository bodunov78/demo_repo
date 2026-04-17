



from itertools import *

# for n in range(1,5+1):
#     for x in product("01",repeat=n):
#         print ("".join(x))
m=["".join(x) for n in range(1,5+1) for x in product("01",repeat=n)]
print (m)
n=[ '00', '01', '10', '000', '001', '010', '100', '101', '110', '111', '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111']
k=[]
for a,b in permutations(n,2):
    if a.startswith(b):
        k.append(a)
        print (a,b)
print (k,set(k),len(n))