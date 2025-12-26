# 14:05
i=6*343**5+5*49**7-50
s=""
while i >0:
    s=str(i%7)+s
    i=i//7

print (s.count('6'))
# 14:06
