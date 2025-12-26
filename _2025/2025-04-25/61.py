from turtle import *
from math import *

screensize(2000, 1500)
def vsum(v1,v2):

    return (v1[0]+v2[0],v1[1]+v2[1])

def sq(p1,p2,p3):
    d1 = dist( p1, p2)
    d2 = dist( p2, p3)
    d3 = dist( p1 ,p3)
    p = (d1 + d2 + d3) / 2
    s = (p * (p - d1) * (p - d2) * (p - d3)) ** 0.5
    return s




print (vsum((1,1),(1,-5)))
k=40
# speed(5)
begin_poly()
print(position())
# rt(15)
# for i in range(5):
#
#     fd(5*k)
#     rt(360/5)
#     print(position())

for i in range(2):
    fd(27*k)
    rt(90)
    fd(8*k)
    rt(90)




end_poly()
# print(get_poly())
a=get_poly()
a=list(a)[:-1]

dists=[]
print (a)
for p1 in list(a):
    d=0
    for p2 in list(a):
        d+=dist(p1,p2)
    dists.append((d,p1))
print (max(dists)[0],dists)
maxd=max(dists)[0]
print (maxd)

# s=0
# for p1,p2 in zip(a[1:],a[2:]):
#     print (p1,p2)
#     d1=dist(a[0],p1)
#     d2 = dist(a[0], p2)
#     d3 = dist( p1,p2)
#     p=(d1+d2+d3)/2
#     # s+=(p*(p-d1)*(p-d2)*(p-d3))**0.5
#     s+=sq(a[0],p1,p2)
# print("square",round(s,5))
# print(a)
# up()
# cnt=0
# di=set()
# for x in range(-10*k,10*k,k):
#     for y in range(-20*k,20*k,k):
#         s1=0
#         for p1,p2 in zip(a,a[1:]):
#
#             s1+=sq((x,y),p1,p2)
#             if abs(s1-s)<0.1:
#                 di.add((x,y))
#                 cnt+=1
#                 print ("OK", x,y,s1,cnt)
#                 goto(x,y)
#                 dot(5,"red")
#             # else:
#             #     goto(x, y)
#             #     dot(4, "blue")
#
# print (di,len(di))
# #
# for x in range(-10*k,10*k,k):
#     for y in range(-10*k,10*k,k):
#         goto(x,y)
#         dot(3,"red")
up()
di=set()
cnt=0
for x in range(-10*k,10*k,k):
    for y in range(-15*k,5*k,k):
        s1=0
        for p1 in a:
            s1=s1+dist((x,y),p1)
        if s1<=maxd:
            di.add((x,y))
            cnt+=1
            print ("OK", x,y,s1,cnt)
            goto(x,y)
            dot(5,"red")
        else:
            goto(x, y)
            dot(4, "blue")




done()
