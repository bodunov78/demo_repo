m = 0
P = set( range(5, 31))
Q = set( range(14, 24))



print (P,Q)







for Amin in range(1, 100):
    for Amax in range(Amin + 1, 101):
        check = 1
        A = {i for i in range(Amin, Amax)}
        print (A)

        for x in range(1, 101):
            f = ((x in P) == (x in Q)) <= (not(x in A))
            if not f:
                check = 0
                break
        if check == 1:
            m = max(m, Amax - Amin)
print(m)