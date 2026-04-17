a=dict()

a=[1,2,3,4,5,6]
b=[0,3,5,7,9,0]
# a=dict(zip(a,b))
# print (a)
# for x,y in zip(a,b):
#     print (x,y)

for a1,a2,a3 in zip(a,a[1:],a[2:]):
    print (a1,a2,a3)
# 1 0
# 2 3
# 3 5
# 4 7
# 5 9
# 6 0