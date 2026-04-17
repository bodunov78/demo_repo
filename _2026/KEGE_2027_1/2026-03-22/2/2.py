with open("1.txt") as f:
    cnt=0
    for x in f:
        cnt+=1

        print (cnt,int(x))