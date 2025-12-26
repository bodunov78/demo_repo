from math import *

#27771-27773

def f(a,b,m):
    if a+b <=20: return m%2 ==0
    if m==0 : return 0
    # останется на 1 камень больше
    # h=[f(a-1,b,m-1),f(a,b-1,m-1),f(ceil(a/2),b,m-1),f(a,ceil(b/2),m-1)]
    # останется на 1 камень меньше
    h = [f(a - 1, b, m - 1), f(a, b - 1, m - 1), f(a // 2, b, m - 1), f(a, b // 2, m - 1)]

    return any(h) if (m-1)%2 ==0 else all(h)

#27774-27776

def f4(a,b,m):
    if a+b <=20: return m%2 ==0
    if m==0 and a+b >20 : return 0
    # останется на 1 камень больше
    h=[f(a-1,b,m-1),f(a,b-1,m-1),f(ceil(a/2),b,m-1),f(a,ceil(b/2),m-1)]
    # останется на 1 камень меньше
    # h = [f(a - 1, b, m - 1), f(a, b - 1, m - 1), f(a // 2, b, m - 1), f(a, b // 2, m - 1)]

    return any(h) if (m-1)%2 ==0 else all(h)


print ("19:",[s for s in range(11,100) if f(s,10,2) ])
print ("20:",[s for s in range(11,100) if (not f(s,10,1)) and f(s,10,3) ])
print ("21:",[s for s in range(11,100) if ( f(s,10,2)) or f(s,10,4) ])


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

#
#
# #27797
# #27798
# #27799
#
def f(a,b,m):
    if a+b >=68: return m%2 ==0
    if m==0 : return 0
    h=[f(a+1,b,m-1),f(a,b+1,m-1),f(a*3,b,m-1),f(a,b*3,m-1),]
    return any(h) if (m-1)%2 ==0 else all(h) # any 19/all 20-21


print ("19:",[s for s in range(1,61+1) if f(s,6,2) ])
print ("20:",[s for s in range(1,61+1) if (not f(s,6,1)) and f(s,6,3) ])
print ("21:",[s for s in range(1,61+1) if (not f(s,6,2)) and f(s,6,4) ])
#
#
#
#
#
# # def f(a,b,c,m):
# #     if a+b<= 20: return c%2 == m%2
# #     if c==m: return 0
# #     h=[f(a-1,b,c+1,m),f(a,b-1,c+1,m),f(ceil(a/2),b,c+1,m),f(a,ceil(b/2),c+1,m),]
# #     return any(h) if (c+1)%2 ==m%2 else any(h)
# # for a in range(11,100):
# #     for m in range(1,5):
# #         if f(a,10,0,m) ==1:
# #             print(a,m)
# #             break

# 68281
def f(a,m):
    if a >40: return m%2 ==0
    if m==0 : return 0
    h=[f(a+(a//k),m-1) for k in range(1,a+1) if a%k==0 and k>1]
    # h2=[(a+(a//k),m-1) for k in range(2,a+1) if a%k==0]
    # print (a,h2)
    # В начале игры в куче было S камней, S≤40. Укажите количество таких значений S,
    # при которых Петя не может выиграть первым ходом,
    # но при любом первом ходе Пети Ваня может выиграть своим первым ходом.
    return any(h) if (m-1)%2 ==0 else all(h)


print ("19:",[s for s in range(2,40+1) if  f(s,2) ])
print ("20:",[s for s in range(2,40+1) if (not f(s,1)) and f(s,3) ])
print ("21:",[s for s in range(2,40+1) if (not f(s,2)) and f(s,4) ])
