#1
ch=bin(127)[2:]
print(ch)
#2
ch=127
res=""
while ch>0:
    res=str(ch%2)+res
    ch=ch//2
    print(ch)
