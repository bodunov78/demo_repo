from itertools import *
s="ТИМОФЕЙ"
a=list(product(s,repeat=5))
cnt=0
for x in a:
   s= "".join(x)

   if s.count("Й") ==1 and 0<s.index("Й")<4 and s.count("ИЙ")==0 and s.count("ЙИ")==0 :
      cnt+=1
      #print(s)
   elif x.count("Й") ==0:
      cnt+=1
      print(s)

print (cnt)

