a=[11, 3,2,10, 1,2, 3,3, 4, 8]
b=[2, 3,3, 4, 8]


def fufu(a,b):
    i,j=0,0
    c=[]
    # print("a,b",a,b)
    while i <=len(a) and j <=len(b):
        if  i < len(a) and j< len(b) and a[i] <= b[j] :
            c.append(a[i])
            i += 1
            # print(1,c)
        elif  i < len(a) and j< len(b) and a[i] > b[j]:
            c.append(b[j])
            j += 1
            # print(2, c)
        elif i == len(a) and j < len(b):
            c.append(b[j])
            j +=1
            # print(3, c)
            # return c
        elif j == len(b) and i < len(a):
            c.append(a[i])
            i +=1
            # print(4, c)
        elif j == len(b) and i == len(a):
            return c
        # print("i,j",i,j,len(a),len(b))
        #     return c
        # else:
        #     return c
def spli(a,srt=1,b=[]):
    if srt == 1:
        for i in range(0, len(a), 2):
            if i + 1 < len(a):
                b.append([min(a[i], a[i + 1]), max(a[i], a[i + 1])])
            else:
                b.append([a[i]])

        # print(b)

        return spli(b,srt=0)
    elif srt ==0:
        # print("srt",len(a[-1]),a[0],a[-1])
        if len(a[-1])==1:
            a[0]=fufu(a[-1],a[0])
            a=a[:-1]
            # print("srt=0",a)
        while len(a)>1:
            a[0]=fufu(a[0],a[1])
            a.pop(1)
            # +a[2:]
            # print("!!!",a)
        else:
            a=a[0]
            return a


# fufu(a,b)
a=list(map(int,input().split()))
print(spli(a,srt=1))
