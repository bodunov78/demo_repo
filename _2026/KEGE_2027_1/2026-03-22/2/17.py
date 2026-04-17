with open("17.txt") as f:
    a=[]
    for s in f:
        s=s.strip()
        a.append(int(s))

    print (len(a))
#
# for i in range(0,len(a)-2):
#     if a[i]+a[i+1]+a[i+2]>100:
#         print ("OK")

for a1,a2,a3 in zip(a,a[1:],a[2:]):
    if a1+a2+a3>100:
        print ("OK")

