f=open("17 (5).txt","r")
f.close()
m=[]
with open("17 (5).txt", "r",encoding="utf-8") as f:
#     for s in f:
#         s=s.strip()
#
#         m.append(int(s))
#     print(m[:10])
# #     # m=[int(x) for x in open("17 (5).txt")]
# #
# #     # s=f.read(1)
# #     # k=f.read(1)
# #     # f.readline()
    m=f.readlines()
    print (m[:10])
#     #
#     print (type(m),len(m),m[:10])
# for x in m:
#
#     k=int(x)
#     print (len(x),k,type(k))
#
#
#

