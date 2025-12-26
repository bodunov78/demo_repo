# with open("DEMO_24.txt") as f:
#     s=f.readline()
#     m=0
#     for l in range(len(s)):
#         for r in range(l+m,len(s)):
#             ss=s[l:r+1]
#             if  ss.count('Y')==80 :
#                 m=max(m,len(ss))
#             else:
#                 break
#     print (m)
#

s = 'Y' + open('DEMO_24.txt').readline() + 'Y'
maxi = 0
n_y = [x for x in range(len(s)) if s[x] == 'Y']
for i in range(len(n_y) - 81):
    if s[n_y[i + 1]: n_y[i+81]].count('2025') >= 90:
        maxi = max(maxi, n_y[i + 81] - n_y[i] - 1)
print(maxi)