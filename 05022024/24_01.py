#Тип 24 27686
# f=open("27686.txt")
# a=f.readline()
# a=a.replace('Y',' ').replace('Z',' ')
# m=a.split()
# m.sort()
# print (m)
# f.close()
#


# f=open("27421.txt")
# a=f.readline()
# a=a.strip()
# while 'XX' in a or 'YY' in a or "ZZ" in a:
#     a=a.replace('XX','X X').replace('YY','Y Y').replace('ZZ','Z Z')
#
# m=[len(x) for x in a.split()]
# print(max(m))


# f = open('27421.txt').readline()
# k = 1
# m = 0
# for i in range(1, len(f)):
#     if f[i] != f[i-1]:
#         k += 1
#     else:
#         m = max(m, k)
#         k = 1
# m = max(m, k)
# print(m)
#
# f=open("27689.txt")
# a=f.readline().strip()
# print (len(a))
# while 'XYZ' in a:
#     a=a.replace('XYZ','QQQ')
# print(a)
# while 'QQQXY' in a:
#     a=a.replace('QQQXY','QQQQQ ')
#
# while 'QQQX' in a:
#     a=a.replace('QQQX','QQQQ ')
#
# while 'X' in a:
#     a=a.replace('X',' ').replace('Y',' ').replace('Z',' ')
#
#
# m=[len(x) for x in a.split()]
# print(max(m))
#
# f=open("29672.txt")
# i=0
# n=f.readline()
# while n:
#
#     if n.count('E')>n.count('A'):
#         i += 1
#     n = f.readline()
#
# print (i)
# f.close()
#
#
# f=open("29672.txt")
# i=0
#
# for n in f:
#     if n.count('E')>n.count('A'):
#         i += 1
# print (i)
# f.close()
#

f=open("33196.txt")

for n in f:
     di={x:0 for x in set(n)}
     print(di)
     for i in range(1,len(n)):
        if n[i-1]=='A':
            di[n[i]]+=1

for key, value in di.items():
    if value==max(di.values()):
        print (key,value)





