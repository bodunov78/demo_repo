def fu1():
    print(1)
    print(2)
    print(3)
    if 1 == 2:
        return "OK"
    print(4)
    print(5)
    #fu2()
    return fu2()





def fu2():
    flag=0
    for x1 in range(100):
        if flag==1:
            break
        for x2 in range(100):
            if flag == 1:
                break
            for x3 in range(100):
                if flag==1:
                    break
                for x4 in range(100):
                    if flag == 1:
                        break
                    for x5 in range(100):
                        if flag == 1:
                            break
                        for x6 in range(100):
                            if flag == 1:
                                break
                            for x7 in range(100):
                                if flag == 1:
                                    break
                                for x8 in range(100):
                                    if flag == 1:
                                        break
                                    for x9 in range(100):
                                        if flag == 1:
                                            break
                                        for x_10 in range(100):
                                            if x7>x1<x8:
                                                print (x7,x1,x8)
                                                return (x7,x1,x8)


def fu3(n):

    print ("fu3",n)
    if n < 999:
        fu4(n + 1)
    # return fu4()


def fu4(n):
    print("fu4",n)
    if n <999:
        return fu4(n+1)


fu4(1)
print ("Жизнь после жизни...")
# print (fu2())

#print(fu1())
