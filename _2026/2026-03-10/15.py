def z15(x, A):
    def dela(x, A):
        if x % A == 0:
            return 1
        else:
            return 0

    return (not (dela(x, A))) <= ((dela(x, 6) <= (not (dela(x, 4)))))


for A in range(1, 100):
    m = [z15(x, A) for x in range(1, 100)]
    if all(m) == True:
        print(A)
