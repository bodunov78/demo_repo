with open("55596.txt") as f:
    k=[]
    m=[]
    for s in f:
        arr=list(map(int,s.split()))
        k = k + arr
        # set_arr=set(arr)
        if len(arr)==len(set(arr)):
            # print (arr,set(arr))
            m = m + arr

            print (len(k))
    cnt=0
    for x in set(m):
        cnt=0
        if k.count(x)==46:
            cnt+=1
            print (x,cnt)