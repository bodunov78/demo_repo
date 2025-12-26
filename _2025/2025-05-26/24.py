from string import *
di="0123456789AB"
ch="02468A"
f=open("24_21421.txt")
s=f.readline().strip()
m=0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        # print(set((s[l:r+1]))-set('0123456789AB') )
        ss=s[l:r+1]
        if len(set(ss)-set('0123456789AB'))==0 and ss[0]!='0' and ss[-1] in '02468A':
            m=max(m,len(ss))
            print ("MMM",m)
        else:
            break

print (m)
