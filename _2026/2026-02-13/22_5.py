def fufu(k):

    if len(a[k][1:])>0:
        # print(a[k][1:])
        suma=max(fufu(x) for x in a[k][1:] )+a[k][0]
        return suma


    else:
        return 0

a=dict()
with open("25_5.txt") as f:
    for s in f:
        m=list(map(int,s.split()))
        a[m[0]]=m[1:]

print (a)


for k,v in a.items():
    # print (k,v)
    print(k,fufu(k))

#
# a[5]=[2,3,4,5]
# print (a[5][2])
# # a=5
# # b=a
# # s=f"{a}+2+{b}"
# # print (eval(s))
