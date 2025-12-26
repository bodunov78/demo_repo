from math import *
# def f(a,b,m):
#     if a+b <=20: return m%2 ==0
#     if m==0 : return 0
#     h=[f(a-1,b,m-1),f(a,b-1,m),f(ceil(a/2),b,m-1),f(a,ceil(b/2),m-1)]
#     return any(h) if (m-1)%2 ==0 else any(h)
#
#
# print ("19:",[s for s in range(120,200) if f(s,10,2) ])
# print ("20:",[s for s in range(1,65) if (not f(s,10,1)) and f(s,10,3) ])
# print ("21:",[s for s in range(1,65) if (not f(s,10,2)) and f(s,10,4) ])


# 27814
# 27815
# 27816
def f(a,m):
    if a >=70: return m%2 ==0
    if m==0 : return 0
    h=[f(a+1,m-1),f(a+4,m-1),f(a*5,m-1)]
    return any(h) if (m-1)%2 ==0 else all(h)


print ("19:",[s for s in range(1,69+1) if  f(s,2) ])
print ("20:",[s for s in range(1,69+1) if (not f(s,1)) and f(s,3) ])
print ("21:",[s for s in range(1,69+1) if (not f(s,2)) and f(s,4) ])




#
# 27820
# 27821
# 27822
def f(a,m):
    if a >=42: return m%2 ==0
    if m==0 : return 0
    h=[f(a+1,m-1),f(a+2,m-1),f(a*2,m-1)]
    return any(h) if (m-1)%2 ==0 else all(h)


print ("19:",[s for s in range(1,41+1) if f(s,2) ])
print ("20:",[s for s in range(1,41+1) if (not f(s,1)) and f(s,3) ])
print ("21:",[s for s in range(1,41+1) if (not f(s,2)) and f(s,4) ])



#27797
#27798
#27799

def f(a,b,m):
    if a+b >=68: return m%2 ==0
    if m==0 : return 0
    h=[f(a+1,b,m-1),f(a,b+1,m-1),f(a*3,b,m-1),f(a,b*3,m-1),]
    return any(h) if (m-1)%2 ==0 else all(h) # any 19/all 20-21


print ("19:",[s for s in range(1,61+1) if f(s,6,2) ])
print ("20:",[s for s in range(1,61+1) if (not f(s,6,1)) and f(s,6,3) ])
print ("21:",[s for s in range(1,61+1) if (not f(s,6,2)) and f(s,6,4) ])





# def f(a,b,c,m):
#     if a+b<= 20: return c%2 == m%2
#     if c==m: return 0
#     h=[f(a-1,b,c+1,m),f(a,b-1,c+1,m),f(ceil(a/2),b,c+1,m),f(a,ceil(b/2),c+1,m),]
#     return any(h) if (c+1)%2 ==m%2 else any(h)
# for a in range(11,100):
#     for m in range(1,5):
#         if f(a,10,0,m) ==1:
#             print(a,m)
#             break
