with open("47213.txt") as f:
    cnt=0
    for x in f:
        arr=list(map(int,x.split()))
        sum_p=0
        sum_np=0
        if len(set(arr))==5:
            for j in set(arr):
                if arr.count(j)==2:
                    sum_p=j*2
                else:
                    sum_np+=j
            if sum_np/4 <= sum_p:
                cnt+=1
                print (cnt, sum_p, sum_np)



            print (arr)
        # s=[arr.count(y) for y in set(arr)]
        # print (s,arr)
        #
        # if len(arr)==len(set(arr)):
        #     print (arr)