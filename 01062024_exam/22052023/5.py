
for i in range(1000):
   s=bin(i)[2:][::-1]
   if int(s,2) ==11:
      print(i,s,int(s,2))