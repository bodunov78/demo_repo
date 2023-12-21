from itertools import *

s={x for x in product([1,2,22],repeat=4)}
print (s)
arr = [[] for x in range(4)]


print (id(arr[0]),id(arr[1]),id(arr[2]),id(arr[3]),)
for km in range(1,38):

    arr = [[] for x in range(4)]
    print(km,arr)

    for ss in s:
        # print(f"ss{ss}")
        ku = km

        for i,v in enumerate(ss):
            # print (i,v)
            if v == 1:
                ku += 1
            elif v == 2:
                ku += 2
            elif v == 22:
                ku *= 2
            #arr[i].append(ku)

            # print (f"ss {ss} i {i} ku {ku} arr[{i}] {arr[i]}")
            arr[i].append(ku)
    ars=[]
    for i in range(len(arr[0])):
        # if arr[0][i]<38 and arr[2][i] <38 and (arr[1][i] >=38 or arr[3][i]>=38):
        if arr[0][i] < 38 and arr[2][i] >= 38 and (arr[1][i] < 38):

            ars.append(ss)


    print(km,len(arr[0]),len(ars),ars)
