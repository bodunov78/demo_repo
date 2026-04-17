def f2():
    #  это супер пупер замечательная программа
    cnt=0
    a=[]
    # flag=0
    for a1 in range(5):
        # if flag==1:
        #     break
        for a2 in range(5):
            # if flag == 1:
            #     break

            for a3 in range(5):
                # if flag == 1:
                #     break

                for a4 in range(5):
                    if (a1+a2)==(a3+a4):
                        cnt+=1
                        a.append((a1,a2,a3,a4))
                        # print (a1,a2,a3,a4)
                        if cnt==4:
                            return a

print (f2())

for i in range(10+1):
    print (i)

for i in range(2,10+1):
    print (i)

for i in range(10,0-3,-3):
    print (i)

for c in "asdfghjkl":
    print (c)

a=[1,2,3,44,4,6,4,4,0,44]
for d in set(a):
    print (d)

