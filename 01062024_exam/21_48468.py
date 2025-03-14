from math import *

# 48468
# 63069
# 63070
def f(a,m):
    if a >=151: return m%2 ==0
    if m==0 : return 0
    # h=[f(a+1,m-1),f(a+4,m-1),f(a*5,m-1)]
    h=[]
    if (a+1)%3 !=0:
        h.append(f(a+1,m-1))
    if (a + 2) % 3 != 0:
            h.append(f(a + 2, m - 1))
    if (a *2) % 3 != 0:
            h.append(f(a*2, m - 1))

        # при любом ходе пети ставим all
    return any(h) if (m-1)%2 ==0 else all(h)


print ("19:",[s for s in range(1,149+1) if  f(s,2) ])
print ("20:",[s for s in range(1,149+1) if (not f(s,1)) and f(s,3) ])
print ("21:",[s for s in range(1,149+1) if (not f(s,2)) and f(s,4) ])
# Для того, чтобы Петя выиграл своим вторым ходом при любой игре Вани, Петя должен получить своим первым ходом число 74.
#
# Получить 74 своим первым ходом можно из значений 37, 72 и 73.
#
# Число 72 не подходит, так как делиться на 3.
#
# Рассмотрим число 73. Своим первым ходом Петя прибавляет один камень куче и делает S=74,
# тогда Ваня может получить значения 76 и 148 (75 не подходит, так как делится на 3).
# Во всех случаях Петя увеличивает количество камней в куче в два раза и выигрывает своим вторым ходом.



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
