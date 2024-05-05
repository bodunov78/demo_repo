from itertools import *
def f(x, y, z, w):
    # ((y → z) ∨ (¬x ∧ w)) ≡ (w ≡ z)
    return (((y<=z) or (not(x) and w)) == (w==z))

#18550
def vah():
    for a1, a2, a3 in product([0, 1], repeat=3):
        tab = [(a1, 1, 0, 0), (0, 0, 0, 1), (0, 1, a2, a3)]
        if len(tab) == len(set(tab)):
            for p in permutations('xyzw'):
                if [f(**dict(zip(p, r))) for r in tab] == [1, 1, 1]:
                    print(p)




# vah()
#58510

# Две логические функции заданы выражениями:
# F1=(w∨¬y)→(z≡x)
# F2=(w∨¬y)≡(x→z)


def f1(x, y, z, w):
    return ( (w or not(y)) <= (z==x))
def f2(x, y, z, w):
    return ( (w or not(y)) == (x<=z))

def vah1():
    for a1, a2, a3,a4,a5, a6 in product([0, 1], repeat=6):
        tab = [(a1, 1, a2, 1), (a3, 0, 0, 0), (0, 0, 0, a4)]
        if len(tab) == len(set(tab)):
            for p in permutations('xyzw'):
                if ([f1(**dict(zip(p, r))) for r in tab] == [0, a5, 0]) and ([f2(**dict(zip(p, r))) for r in tab] == [a6, 0, 0]):
                    print(p)



vah1()