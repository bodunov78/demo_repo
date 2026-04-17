flag=0
for a1 in range(5):
    if flag==1:
        break
    for a2 in range(5):
        if flag == 1:
            break

        for a3 in range(5):
            if flag == 1:
                break

            for a4 in range(5):
                if (a1+a2)==(a3+a4):
                    print (a1,a2,a3,a4)
                    flag=1
                    break

