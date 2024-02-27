with open("27989_B.txt") as f:
    n=f.readline() # пропуск первой строчки с количеством чисел
    cnt=0
    a2=0
    a13=0
    a26=0
    a0=0
    # f = [2, 6, 13, 39]
    for x in f:
        x=int(x)
        if x%26==0:
            a26+=1
        elif x%13==0:
            a13+=1
        elif x%2==0:
            a2+=1
        else:
            a0+=1
        cnt=a26*(a13+a2+a0)+a13*a2+a26*(a26-1)/2
        print (cnt)

        # a=[2,6,13,39]
