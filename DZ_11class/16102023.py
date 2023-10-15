from itertools import *

s="ABCDEF"
arr=[]
arr2=[]
s=list(combinations(s,3))
#print (s)
for x in s:
    for y in list(permutations(x)):
        arr.append(y)



#print (arr)
cnt=0
for x in arr:
    for y in product(x,repeat=6):
        # cnt+=1
        # print(x,y,cnt)
        if y.count(x[0])==1 and y.count(x[1])==2 and y.count(x[2])==3 :
            cnt += 1
            st="".join(y)
            print(x, y, cnt)

            #print (st)
            arr2.append(st)

print(len(arr2),len(set(arr2)))
for x in arr2:
    if x.count("c")==1:
        print(x)

