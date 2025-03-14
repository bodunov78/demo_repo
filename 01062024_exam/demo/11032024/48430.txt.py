with open("48430.txt") as f:
    cnt=0
    for x in f:
        x=list(map(int,x.split()))
        a=[x.count(c) for c in set(x)]
        a.sort
        if a==[1,1,2,2]:
            snp=0
            spp=0
            print (x,a)
            for c in set(x):
                if x.count(c)==1:
                    snp+=c
                else:
                    spp+=c
            if spp<snp:
                cnt+=1
    print (cnt)

