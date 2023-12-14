from itertools import *
for x1 in ('1','2'):
    for x2 in ('1', '2'):
        for x3 in ('1', '2'):
            for x4 in ('1', '2'):
                for x5 in ('1', '2'):
                        print (x1+x2+x3+x4+x5)

for i in product((1,2),repeat=5):
     print ("".join(str(i)))