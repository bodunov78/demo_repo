with open("26_21910.txt") as f:
    n=f.readline()
    m=[int(a) for a in f]
    m.sort(reverse=1)
    print (m[-10:])
    zep=[0]*len(m)
    # print (zep)

    for i in range(len(m)):
        for j in range(i):
            if m[j]-m[i]>=9:
                zep[i]=max(zep[i],zep[j]+1)
            if zep[i]==0:  zep[i]=1
    print(zep[-10:])

    for i,v in enumerate(zep):
        if v==1040:
            print (m[i])

# f=open("1_26 (2).txt")
# n = f.readline()
# boxes = sorted([int(i) for i in f], reverse=True)
# answer = [boxes[0]]
# for box in boxes[1:]:
#     if answer[-1] - box >= 3:
#         answer.append(box)
# print(len(answer), answer[-1])

# f = open('1_26 (2).txt')
# n = int(f.readline())
# a = [int(i) for i in f]
# a.sort(reverse = True)
# count = 1
# diametr = a[0]
# for i in range(1,len(a)):
#     if diametr - a[i] >= 4:
#         count += 1
#         diametr = a[i]
# print(count,diametr)