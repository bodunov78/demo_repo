from re import *
with open("24_20813.txt") as f:
    # for s in f:
    #     print (len(s))

#
#
#
    s=f.readline()
    ss=s.strip()
    while '-*' in ss or '*-' in ss or '**' in ss or '--' in ss :
        ss=ss.replace('-*','::').replace('*-','::').replace('-:','::').replace('*:','::').replace(':-','::').replace(':*','::').replace('--','::').replace('**','::')

    print(ss[:1000])

    m=[x for x in ss.split(":") if len(x)>0]
    print (m)


    for x in m:
        for i in range(2,len(x)):
            if x[i-2] in [-*] and x[i-1] =='0' and x[i] in [789]:
                k=


        print (len(x),x)



#     num = r"(([789][0789]*|0{1}))"
# #
# #     num=r"(([789][0789]*|0{1}))"
# #     numz = r"(([0789]*|0{1}))"
#     a=[]
# #     AB = r"(AB).*"
# #     numz=r"([1-9][0-9]*|0{1})"
# #     abs=rf{AB}{100}
#     proiz = rf"{num}([*-]{num})*"
#     reg = rf"(?=({proiz}))"
#     for x in finditer(reg, s):
#         a.append(x.group(1))
#         # print(x.group(1))
#     b=[[len(x),x] for x in a]
#     print (max(b))
# #
#     # s=s.strip()
#
#
#
# s="1231231212333112"
# ab=r"12[0,2,3,4,5,6,7][0-9]*"
# proiz=rf"({ab}){3}"
# # reg=rf"(?=({ab}))"
# for x in finditer(proiz,s):
#     print(x.group(1))
#
# m=0
# for l in range(len(s)):
#     for r in range(l+m,len(s)):
#         ss=s[l:r+1]
#         if (ss=='0*' or ss[:2]=='0-' or ss[0] in '789') and '**' not in ss and "*-" not in ss and '--' not in ss and '-*' not in ss  and "*07" not in ss and "*09" not in ss and "*08" not in ss and "-07" not in ss and "-08" not in ss and "-09" not in ss and "*00" not in ss and "-00" not in ss:
#             m=max(m,len(ss))
#             print (ss,len(ss))
#         else:
#             break