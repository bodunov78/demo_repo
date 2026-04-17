cnt=0
for a1 in range(256):
    # print (a1)
    if (162 & 255) != (a1 & 255) :
        continue
    for a2 in range(256):
        if  (198 & 255) != (a2 & 255) :
            continue

        for a3 in range(256):
            if  (0 & 255) != (a3 & 255) :
                continue
            for a4 in range(256):
                if  (157&224)==(a4&224):
                    print (a1,a2,a3,a4,cnt)
                    cnt+=1