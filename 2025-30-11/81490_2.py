from time import *
ts=time()
m2025=[]
y120=[]
with open("81490.txt") as f:
    s=f.readline()
    m=0
    for l in range(len(s)):
        for r in range(l+m,len(s)):
            ss=s[l:r+1]
            if  ss[:4]=='2025' and  ss.count('2025')==60:
                        m2025.append(ss)
                        m = max(m, len(ss))
            elif ss.count('2025')>60:
                break
    print (m)
print (len(m2025))
for s in m2025:
    if s.count('Y')>=120:
        y120.append(s)



print (max(y120),len(max(y120)))
print (time()-ts)


#
# s = open('81490.txt').readline().split('2025')
# maxi = 0
# for i in range(len(s) - 60):
#     st = '2025' + '2025'.join(s[i:i + 60])
#     if st.count('Y') >= 120:
#         if maxi<len(st)+3:
#             maxi = len(st) + 3
#             print (len(st),st)
# print(maxi)