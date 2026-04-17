from itertools import permutations, repeat

s="AB:10,AD:3,BD:10,BE:2,BF:1,CD:2,CF:4,DE:4,BA:10,DA:3,DB:10,DC:2,EB:2,ED:4,FB:1,FC:4"
a=s.replace(':',',').split(',')[::2]
d=s.replace(':',',').split(',')[1::2]

from itertools import *

for i in permutations(a,6):
    # ss="".join(i)
    # if len(set(ss))==len(ss)/2:
    #     print (ss)
    ss="A"
    if i[0][0]=='A' and i[-1][1]=='F':
        if all(i[j][0] == i[j-1][1] for j in range(1,len(i))):
            
            print (i)

# print (a)
# # s = "a=1;b=2;c=3"
# d = {}
# for item in s.split(','):
#     key, value = item.split(':')
#     d[key] = int(value)  # если нужно число
# print(d)