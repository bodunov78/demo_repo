s="0123456789ABCDEF"

n=1000

i=n

ch=""
ost=""
while i>0:
    ost=i%16
    i=i//16
    # ch=str(ost)+ch
    ch=s[ost]+ch
print (n,ch,int(ch,16))
