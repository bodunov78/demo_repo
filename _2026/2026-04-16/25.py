def f(n, d=2):
    for d in range(d, int(n**0.5) + 1):
        if n % d == 0:
            return [d] + f(n//d, d)
    return [n]

k = 0

for x in range(2_300_300, 10**100):
    p_mn = f(x)
    if any(c in p_mn for c in range(11, 100, 11)):
        print(x, max(p_mn))
        k += 1

    if k == 5:
        break
