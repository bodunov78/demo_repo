k=0
p=[3,5,7,11,13,17,19]
for i in range(21,int(102000000**0.5)+1 ,2):
    m=any([ i%x==0 for x in p])
    #print (i,m)
    #print (i,m,a)
    if not m:
        p.append(i)
        print(i, m, p)

print (len(p))
for x in p:
    if 101_000_000<=2*(x**2)<=102_000_000:
        print (x,2*(x**2))

#
# cnt=0
# for i in range(101_000_000,102_000_000+1,2):
#     m1=[]
#     m2=[]
#     for x in p:
#         if i%x==0:
#             m1.append(x)
#             if i%(x**2)==0:
#                 m2.append(x)
#         if len(m1)>1:
#             break
#     if len(m2)==1:
#         cnt+=1
# print(i)
#
#
#
#
