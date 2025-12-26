s="-3X-y-10z=-20"




s=s.lower()

for c in s:
    if c.isalpha():
        print(c)

s=s.replace('+',':').replace('-',':-').replace('=',':').replace('::',':').lstrip(':')
m=s.split(':')

for c in m[:-1]:
    print (c)


for i,c in enumerate(m):

    if c[0]=='-' and i <len(m)-1:
        k=c[1:-1]
        if len(k)==0: k=-1
        else: k=-1*int(c[1:-1])

    elif c[0]!='-' and i <len(m)-1:
        k=int(c[0:-1])
    else:
        k=int(c)
    print (k)

print(s,m)
