f=open("09.csv")
k=f.readline()
a=[]
cnt=0
while k!="":
   k=f.readline()
   b=list(map(int,f.readline().split(';')))
   b.sort()
   if max(b)**2 <min(b)**2 + (sum(b)-min(b)-max(b))**2:
      cnt+=1
      print(b,cnt)

