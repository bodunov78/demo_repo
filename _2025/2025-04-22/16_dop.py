#37871
# N=int(input())
# m=[]
# for i in range(N):
#     x=int(input())
#     if x%2==0:
#         m.append(x)
# print (min(m))

#37837
N=int(input())
m=[]
for i in range(N):
    x=int(input())
    if x%10==4:
        m.append(x)
print (sum(m))
