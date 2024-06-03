from functools import lru_cache


def f(n):
    cisla = []
    for k in range(2, n + 1):
        if n % k == 0:
            cisla.append(n + n // k)
    return cisla


@lru_cache
def game(n):
    if any(x > 40 for x in f(n)):
        return 'vic'
    if all(game(x) == 'vic' for x in f(n)):
        return 'loss1'
    if any(game(x) == 'loss1' for x in f(n)):
        return 'vic2'
    if all(game(x) == 'vic' or game(x) == 'vic2' for x in f(n)):
        return 'loss2'


z_19 = []
z_20 = []
z_21 = []

for n in range(2, 40):
    if game(n) == 'loss1':
        z_19.append(n)
    if game(n) == 'vic2':
        z_20.append(n)
    if game(n) == 'loss2':
        z_21.append(n)

print(z_19)
print(min(z_20), max(z_20))
print(max(z_21))