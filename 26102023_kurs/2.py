# 7763
# На числовой прямой даны два отрезка: P = [5, 30] и Q = [14, 23].
# Укажите наибольшую возможную длину промежутка A, для которого формула
# ((x ∈ P) ≡ (x ∈ Q)) → ¬(x ∈ A)
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.



P=set(range(5,30+1))
Q=set(range(14,23+1))

m = 0
for Amin in range(1, 101):
    for Amax in range(Amin + 1, 101):
        check = 1
        A = set(range(Amin, Amax))
        for x in range(0, 101):
            # f = ((not(x in A)) <= (x in P)) <= ((x in A) <= (x in Q))
            f = ((x in P) == (x in Q)) <=(not(x in A))

            if not f:
                check = 0
                break
        if check == 1:
            m = max(m,Amax - Amin)
            print(A)
print(m - 1)