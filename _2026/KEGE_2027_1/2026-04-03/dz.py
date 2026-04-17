a=[1,2,3,4,5,6,7,8]
# b=a[::2]
# c=a[1::2]
# d=c+b
# print (d)
d=[]
for i in range(0,len(a),2):
    d.append(a[i+1])
    d.append(a[i])
print (d)

d=d[len(a)//2:]+d[:len(a)//2]
print (d)