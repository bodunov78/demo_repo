a="0123456789ABCDEFGH"
# print (a)
d={}
d={k:i for i,k in enumerate(a)}

print (d)

s,i = input().split()
i=int(i)
print (s,i)

s=s[::-1]
j=0
suma=0
print (type (s[0]))
while j < len(s):
   print (d[s[j]])
   suma+=int(d[s[j]])*i**j
   j+=1
   print (suma)