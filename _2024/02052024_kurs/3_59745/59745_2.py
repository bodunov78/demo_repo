# Все 5-буквенные слова, в составе которых могут быть буквы А, Л, Г, О, Р, И, Т, М,
# записаны в алфавитном порядке и пронумерованы начиная с 1.
from itertools import *
s="АЛГОРИТМ"
s=sorted(s)
print (s)
cnt=0
d=0
for m in product(s,repeat=5):
    cnt+=1
    if cnt%2!=0 and m[0]!='Г' and m.count('И')>=2:
        d+=1
        print (m,d,cnt)


