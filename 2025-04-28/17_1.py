#1:23
from re import *
with open("17_19249.txt") as f:
    a=[x for x in f]
    # print (len(a))
    m=[]
    n=[]
    z=[]
    cnt=0
    for x in a:
        x=x.strip()
        # print (x)
        if (len(x) == 5 and x[-2:] == '43' and x[-1]!='-') or (len(x) == 6 and x[-2:] == '43' and x[-1]=='-'):
            n.append(int(x))

            # print(n[-1])
    maxi=max(n)
    print (maxi)

    pat = "[!-]????"
    pat2 = "[!-]????"
    # pat3 = "[!-]????,-?????"
    # pat4 = "^\D*\d{5}\D*$"
    # pat5 = "^[\D*,-]\d{5}\D*$"
    pat6 = "^-\d{3}43$|^\d{3}43$"
    # if fnmatch(a,pat) or fnmatch(a,pat2):
    #     print(a)
    # if filter(a,pat):
    #     print(filter(a,pat3))

    # if match(pat6,a):
    #     print(match(pat4,a))
    # k = [str(a) for a in range(-99999, 100000) if len(str(abs(a))) == 5 and str(a)[-2:] == '43']
    # print(len(k))
    #
    # if any(1 if x in k else 0 for x in b):
    #     print(b, "for")

    # if any(1 if match(pat6, x) else 0 for x in b):
    #     print(b)



    cnt=0
    mini=+10**20
    #
    for a1,a2,a3 in zip(a,a[1:],a[2:]):
        b = [a1.strip(),a2.strip(),a3.strip()]
        # print(b)
        if any(1 if match(pat6, x) else 0 for x in b):
            # print(b)
            k=int(b[0])**2+int(b[1])**2+int(b[2])**2
            if k<=maxi**2:
                cnt+=1
                mini=min(mini,k)
                print (b,cnt,mini)

                # cnt+=1
    #     if (10000<=abs(int(a1))<100000 and a1[-2:]=='43') or (10000<=abs(int(a2))<100000 and a2[-2:]=='43') or (10000<=abs(int(a1))<100000 and a3[-2:]=='43'):
    #
    #         j=int(a1)**2+int(a2)**2+int(a3)**2
    #         print(j)
    #         if j <= maxi**2:
    #             cnt+=1
    #             z.append(j)
    #
    #
    # print (cnt,type(z))

