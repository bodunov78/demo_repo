# F=(!Av!B) & !(!Av!C)


print ("A","B","C","F")
# for A in (0,1):
#     for B in (0,1):
#         for C in (0,1):
#             F=(not (A) or not (B)) and (not (not (A) or not (C)))
#             if (not (A) or not (B)) and (not (not (A) or not (C))):
#                 print (A,B,C,1)
#             else:
#                 print (A,B,C,0)
#



# for A in (0,1):
#     for B in (0,1):
#         for C in (0,1):
#             if (not(A) or not(B)) and (not( not(A) or not(C)) ):
#                 print (A,B,C,1)
#             else:
#                 print (A,B,C,0)
#
#
# from itertools import *
#
# for A,B,C in product([0,1],repeat=3):
#     if (not (A) or not (B)) and (not (not (A) or not (C))):
#         print(A, B, C, 1)
#     else:
#         print(A, B, C, 0)
#
#




from itertools import *
# F=(!Av!B) & !(!Av&!C)
#
# # print ("A","B","C","F")
# for A in ('0','1'):
#     for B in ('0','1'):
#         for C in ('0','1'):
#             for D in ('0','1'):
#                 s=A+B+C+D
#                 print (A,B,C,D,s,int(s,2))


    #
    # for B in (0,1):
    #     for C in (0,1):
    #
    #
#
#             if (not(A) or not(B)) and (not ( (not(A) or not(C)))):
#                 print (A,B,C,1)
#             else:
#                 print (A,B,C,0)
#
#
from itertools import *
print ("A","B","C","F")
for A,B,C in product([0,1],repeat=3):
    F=(not (A) or not (B)) and (not (not (A) or not (C)))
    print (A,B,C,int(F))
#     if (not (A) or not (B)) and (not ((not (A) or not (C)))):
#         print(A, B, C, 1)
#     else:
#         print(A, B, C, 0)
# #
